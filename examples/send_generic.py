import logger
import logging
from fb_messenger.client import FBMessenger
from fb_messenger import attachments
from const import ACCESS_TOKEN, RECIPIENT_ID

LOGGER = logger.get_logger(__name__)

client = FBMessenger(ACCESS_TOKEN, logger_level=logging.DEBUG)

button1 = attachments.ButtonWithWebUrl('title1', 'https://google.com.ua')
button2 = attachments.ButtonWithPostback('title2', 'POSTBACK1')

buttons = attachments.Buttons('buttons group', buttons=(button1, button2))

generic_item1 = attachments.GenericElement(
    title='title1',
    image_url='http://solarviews.com/raw/earth/bluemarblewest.jpg',
    subtitle='subtitle1',
    buttons=(button1, button2),
)

generic_item2 = attachments.GenericElement(
    title='title2',
    image_url='http://solarviews.com/raw/earth/bluemarblewest.jpg',
    subtitle='subtitle2',
    buttons=(button2, button1),
)

generic = attachments.Generic((generic_item1, generic_item2))

response = client.send_attachment(RECIPIENT_ID, generic)
LOGGER.debug(response)
