"""
All action types
:see https://developers.facebook.com/docs/messenger-platform/send-api-reference/sender-actions
"""
from __future__ import unicode_literals

MARK_SEEN = 'mark_seen'
TYPING_ON = 'typing_on'
TYPING_OFF = 'typing_off'

ALL_ACTIONS = (
    MARK_SEEN,
    TYPING_ON,
    TYPING_OFF,
)
