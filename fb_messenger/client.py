from __future__ import unicode_literals

from fb_messenger.interfaces import IFBPayload
from six import string_types
import const
import requests
from response import Response
from .exceptions import FBRequestFailed
import notification_type as nt
import logging


def create_logger():
    """
    Get a logger for the given name, and set the level to match
    that of the LOGGINGLEVEL env var.
    """
    logging.basicConfig()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.WARNING)
    return logger


def validate_callbacks(logger, callbacks):
    if not isinstance(callbacks, dict):
        logger.warn('The second parameter should be a dictionary.')
    for callback in ['authentication', 'received', 'delivery', 'postback']:
        if callback not in callbacks:
            logger.warn('The \'' + callback + '\' action is missing.')
    for callback in callbacks.keys():
        if not hasattr(callbacks[callback], '__call__'):
            logger.warn('The \'' + callback +
                        '\' action should be a function.')
    return callbacks


def get_dict_for_message(recipient_id, attachment, notification_type):
    data = {
        'recipient': {
            'id': recipient_id,
        },
        'message': {},
        'notification_type': notification_type,
    }

    if isinstance(attachment, string_types):
        data['message']['text'] = attachment
    elif isinstance(attachment, IFBPayload):
        data['message']['attachment'] = attachment.get_dict()
    else:
        raise TypeError('Attachment must be string or implements IFBPayload')

    return data


class FBMessenger(object):
    def __init__(self, access_token, callbacks, logger=None, logger_level=None):
        if logger is not None:
            self.logger = logger
        else:
            self.logger = create_logger()

        if logger_level is not None:
            self.logger.setLevel(logger_level)

        self.access_token = access_token
        self.callbacks = validate_callbacks(self.logger, callbacks)

    def send(self, recipient_id, attachment, notification_type=nt.REGULAR):
        data = get_dict_for_message(recipient_id, attachment, notification_type)

        self.logger.debug(data)

        r = requests.post(
            url='{}?access_token={}'.format(const.API_FB_MESSAGES_URL, self.access_token),
            json=data,
        )

        if r.status_code >= 300:
            self.logger.warn(r.text)
            raise FBRequestFailed(r.text)

        return Response(response=r.json())

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
