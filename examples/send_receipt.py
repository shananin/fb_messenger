import logger
import logging
from fb_messenger.client import FBMessenger
from fb_messenger import attachments
from const import ACCESS_TOKEN, RECIPIENT_ID

LOGGER = logger.get_logger(__name__)

client = FBMessenger(ACCESS_TOKEN, logger_level=logging.DEBUG)

receipt_element1 = attachments.ReceiptSubElement(
    title='title1',
    subtitle='subtitle1',
    quantity=1,
    price=12.00,
    currency='USD',
    image_url='http://solarviews.com/raw/earth/bluemarblewest.jpg'
)

receipt_element2 = attachments.ReceiptSubElement(
    title='title2',
    subtitle='subtitle2',
    quantity=2,
    price=14.00,
    currency='USD',
    image_url='http://solarviews.com/raw/earth/bluemarblewest.jpg'
)

summary = attachments.Summary(
    total_cost=30.00,
    subtotal=26.00,
    shipping_cost=3.00,
    total_tax=1.00,
)

receipt = attachments.Receipt(
    recipient_name='name',
    order_number='xxx1',
    currency='USD',
    payment_method='Visa',
    summary=summary,
    receipt_sub_elements=(receipt_element1, receipt_element2),
)

response = client.send_attachment(RECIPIENT_ID, receipt)
LOGGER.debug(response)
