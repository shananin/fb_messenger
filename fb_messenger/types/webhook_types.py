"""
All webhook types
:see https://developers.facebook.com/docs/messenger-platform/webhook-reference
"""
from __future__ import unicode_literals

MESSAGE_RECEIVED = 'message_received'
POSTBACK_RECEIVED = 'postback_received'
AUTHENTICATION = 'authentication'
ACCOUNT_LINKING = 'account_linking'
MESSAGE_DELIVERED = 'message_delivered'
MESSAGE_READ = 'message_read'
MESSAGE_ECHO = 'message_echo'

ALL_WEBHOOKS = (
    MESSAGE_RECEIVED,
    POSTBACK_RECEIVED,
    AUTHENTICATION,
    ACCOUNT_LINKING,
    MESSAGE_DELIVERED,
    MESSAGE_READ,
    MESSAGE_ECHO,
)
