from __future__ import unicode_literals
from fb_messenger.interfaces import IFBPayload
from six import string_types

import logging


def get_logger():
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
