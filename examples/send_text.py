from __future__ import unicode_literals
import logger
from fb_messenger.client import FBMessenger
from const import ACCESS_TOKEN, RECIPIENT_ID

LOGGER = logger.get_logger(__name__)

client = FBMessenger(ACCESS_TOKEN)

response = client.send_attachment(RECIPIENT_ID, 'hello')

LOGGER.debug(response)
