import logger
import logging
from fb_messenger.client import FBMessenger
from fb_messenger import attachments
from const import ACCESS_TOKEN, RECIPIENT_ID

LOGGER = logger.get_logger(__name__)

client = FBMessenger(ACCESS_TOKEN, logger_level=logging.DEBUG)

image = attachments.Image('http://solarviews.com/raw/earth/bluemarblewest.jpg')
response = client.send_attachment(RECIPIENT_ID, image)
LOGGER.debug(response)
