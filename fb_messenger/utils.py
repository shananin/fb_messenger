from __future__ import unicode_literals
from six import string_types
import logging
from fb_messenger.interfaces import IFBPayload


def get_logger():
    """
    Get a logger for the given name, and set the level to match
    that of the LOGGINGLEVEL env var.
    """
    logging.basicConfig()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.WARNING)
    return logger


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
        data['message']['attachment'] = attachment.to_dict()
    else:
        raise TypeError('Attachment must be string or implements IFBPayload')

    return data
