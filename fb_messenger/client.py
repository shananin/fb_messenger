from __future__ import unicode_literals
import requests
from .utils import validate_callbacks, get_dict_for_message, get_logger
from . import const
from .response import Response
from .exceptions import FBRequestFailed
from . import notification_type as nt


class FBMessenger(object):
    def __init__(self, access_token, callbacks, logger=None, logger_level=None):
        if logger is not None:
            self.logger = logger
        else:
            self.logger = get_logger()

        if logger_level is not None:
            self.logger.setLevel(logger_level)

        self.access_token = access_token
        self.callbacks = validate_callbacks(self.logger, callbacks)

    def send(self, recipient_id, attachment, notification_type=nt.REGULAR):
        data = get_dict_for_message(recipient_id, attachment, notification_type)

        self.logger.debug(data)

        request = requests.post(
            url='{}?access_token={}'.format(const.API_FB_MESSAGES_URL, self.access_token),
            json=data,
        )

        if request.status_code >= 300:
            self.logger.warn(request.text)
            raise FBRequestFailed(request.text)

        return Response(response=request.json())

    def create_welcome_message(self, page_id, message):
        message = message.to_dict()

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
