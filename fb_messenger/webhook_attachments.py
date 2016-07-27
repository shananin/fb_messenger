"""
:see https://developers.facebook.com/docs/messenger-platform/webhook-reference/message-received
"""
from __future__ import unicode_literals

from .types import webhook_attachment_types


def parse_payload(payload):
    """
    :type payload: dict
    """
    attachment_type = payload.get('type')

    if attachment_type == webhook_attachment_types.IMAGE:
        return Image(payload)
    elif attachment_type == webhook_attachment_types.AUDIO:
        return Audio(payload)
    elif attachment_type == webhook_attachment_types.VIDEO:
        return Video(payload)
    elif attachment_type == webhook_attachment_types.FILE:
        return File(payload)
    elif attachment_type == webhook_attachment_types.LOCATION:
        return Location(payload)

    return


class Multimedia(object):
    def __init__(self, attachment_payload):
        self.payload = attachment_payload
        self.url = attachment_payload['payload'].get('url')

    def __str__(self):
        return str(self.payload)

    def __unicode__(self):
        return self.__str__()

    def __repr__(self):
        return str(self.__dict__)


class Location(object):
    type = webhook_attachment_types.LOCATION

    def __init__(self, attachment_payload):
        self.payload = attachment_payload
        self.lat = attachment_payload['coordinates'].get('lat')
        self.long = attachment_payload['coordinates'].get('long')

    def __str__(self):
        return str(self.payload)

    def __unicode__(self):
        return self.__str__()

    def __repr__(self):
        return str(self.__dict__)


class Image(Multimedia):
    type = webhook_attachment_types.IMAGE


class Audio(Multimedia):
    type = webhook_attachment_types.AUDIO


class Video(Multimedia):
    type = webhook_attachment_types.VIDEO


class File(Multimedia):
    type = webhook_attachment_types.FILE
