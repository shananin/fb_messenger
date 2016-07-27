from __future__ import unicode_literals
import logger
from fb_messenger.client import FBMessenger
from fb_messenger import attachments
from const import ACCESS_TOKEN, RECIPIENT_ID

LOGGER = logger.get_logger(__name__)

client = FBMessenger(ACCESS_TOKEN)

quick_reply = attachments.QuickReply('Hi!', 'HI')
text = attachments.Text('hello!', [quick_reply])

response = client.send_attachment(RECIPIENT_ID, text)

LOGGER.debug(response)
