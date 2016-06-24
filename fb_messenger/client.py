import const
import logger
import requests
from response import Response
from .exceptions import FBRequestFailed

LOGGER = logger.get_logger(__name__)


class FBMessenger(object):

    def __init__(self, access_token):
        self.access_token = access_token

    def send_message(self, message):
        LOGGER.debug(message.get_dict())

        r = requests.post(
            url='{}?access_token={}'.format(const.API_FB_MESSAGES_URL, self.access_token),
            json=message.get_dict(),
        )

        if r.status_code >= 300:
            LOGGER.debug(r.text)
            raise FBRequestFailed()
        LOGGER.debug((r.status_code, r.text))

        return Response(response=r.json()).parse()

    def create_welcome_message(self, page_id, message):
        message = message.get_dict()

        del message['recipient']
        del message['notification_type']

        data = {
            'setting_type': 'call_to_actions',
            'thread_state': 'new_thread',
            'call_to_actions': [
                message,
            ],
        }

        r = requests.post(
            url='https://graph.facebook.com/v2.6/{}/thread_settings?access_token={}'.format(page_id, self.access_token),
            json=data,
        )

        return r.json()
