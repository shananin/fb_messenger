"""
All types of notification
:see Payload -> notification_type https://developers.facebook.com/docs/messenger-platform/send-api-reference
"""
from __future__ import unicode_literals

REGULAR = 'REGULAR'
SILENT_PUSH = 'SILENT_PUSH'
NO_PUSH = 'NO_PUSH'

ALL_NOTIFICATION_TYPES = (
    REGULAR,
    SILENT_PUSH,
    NO_PUSH,
)
