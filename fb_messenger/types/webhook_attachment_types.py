"""
:see https://developers.facebook.com/docs/messenger-platform/webhook-reference/message-received
"""
from __future__ import unicode_literals

IMAGE = 'image'
AUDIO = 'audio'
VIDEO = 'video'
FILE = 'file'

LOCATION = 'location'

ALL_ATTACHMENT_TYPES = (
    IMAGE,
    AUDIO,
    VIDEO,
    FILE,
    LOCATION,
)
