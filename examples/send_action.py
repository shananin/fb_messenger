import logger
import logging
from fb_messenger.types import action_types
from fb_messenger.client import FBMessenger
from const import ACCESS_TOKEN, RECIPIENT_ID

LOGGER = logger.get_logger(__name__)

client = FBMessenger(ACCESS_TOKEN, logger_level=logging.DEBUG)

response = client.send_action(RECIPIENT_ID, action_types.MARK_SEEN)
LOGGER.debug(response)
