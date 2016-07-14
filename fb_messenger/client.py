from __future__ import unicode_literals
import requests
from fb_messenger.utils import get_dict_for_message, get_logger
from fb_messenger import const
from fb_messenger.response import Response
from fb_messenger.exceptions import RequestFailed
from fb_messenger import notification_type as nt
from fb_messenger import callbacks
from fb_messenger import callback_types


class FBMessenger(object):
    """
    client = FBMessenger(access_token='ADSD...')

    try:
        response = client.send_text('1231313', 'text')
    except MainException as e:
        logging.debug(e)

    attachment = attachments.Image(img_url='http://example.com/img.jpg')
    try:
        response = client.send_attachment('1231313', attachment)
    except MainException as e:
        logging.debug(e)
    """

    _callbacks = {}

    def __init__(self, access_token, logger=None, logger_level=None):
        if logger is not None:
            self.logger = logger
        else:
            self.logger = get_logger()

        if logger_level is not None:
            self.logger.setLevel(logger_level)

        self.access_token = access_token

    def send_attachment(self, recipient_id, attachment, notification_type=nt.REGULAR):
        data = get_dict_for_message(recipient_id, attachment, notification_type)

        self.logger.debug(data)

        request = requests.post(
            url='{}?access_token={}'.format(const.API_FB_MESSAGES_URL, self.access_token),
            json=data,
        )

        if request.status_code >= 300:
            self.logger.warn(request.text)
            raise RequestFailed(request.text)

        return Response(response=request.json())

    def send_text(self, recipient_id, text, notification_type=nt.REGULAR):
        data = get_dict_for_message(recipient_id, text, notification_type)

        self.logger.debug(data)

        request = requests.post(
            url='{}?access_token={}'.format(const.API_FB_MESSAGES_URL, self.access_token),
            json=data,
        )

        if request.status_code >= 300:
            self.logger.warn(request.text)
            raise RequestFailed(request.text)

        return Response(response=request.json())

    def process_message(self, body):
        self.logger.debug(body)

        if 'received' in self._callbacks:
            self._callbacks['received'](body)

    def callback(self, callback_name):
        def decorator(function):
            if callback_name not in callback_types.ALL_CALLBACKS:
                self.logger.warn('{} is not fb messenger callback'.format(callback_name))
                return function

            self.logger.info('{} callback has been added'.format(callback_name))
            self._callbacks[callback_name] = function
            return function

        return decorator

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

        request = requests.post(
            url='https://graph.facebook.com/v2.6/{}/thread_settings?access_token={}'.format(page_id, self.access_token),
            json=data,
        )

        return request.json()
