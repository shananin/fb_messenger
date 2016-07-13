from __future__ import unicode_literals
import json
from fb_messenger import const
from fb_messenger.exceptions import FBIncorrectResponse


class Response(object):
    recipient_id = None
    message_id = None

    def __init__(self, response):
        response = json.loads(response)
        self.response = response

        if const.RECIPIENT_ID_KEY not in response or const.RECIPIENT_ID_KEY not in response:
            raise FBIncorrectResponse("Response doesn't contain {} or {}".format(
                const.RECIPIENT_ID_KEY, const.MESSAGE_ID_KEY
            ))

        self.recipient_id = self.response[const.RECIPIENT_ID_KEY]
        self.message_id = self.response[const.RECIPIENT_ID_KEY]
