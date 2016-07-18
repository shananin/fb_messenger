import logging
from fb_messenger import action_types
from fb_messenger.client import FBMessenger

# ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
recipient_id = '1447507518611413'

client = FBMessenger(ACCESS_TOKEN, logger_level=logging.DEBUG)

response = client.send_action(recipient_id, action_types.MARK_SEEN)
print(response)
