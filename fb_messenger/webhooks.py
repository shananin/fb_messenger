"""
Callbacks parser
"""
from __future__ import unicode_literals
from .types import webhook_types


def parse_payload(payload):
    # pylint: disable=too-many-return-statements
    if 'message' in payload:
        return MessageReceived(payload)
    elif 'delivery' in payload:
        return MessageDelivered(payload)
    elif 'read' in payload:
        return MessageRead(payload)
    elif 'postback' in payload:
        return Postback(payload)
    elif 'optin' in payload:
        return Authentication(payload)
    elif 'account_linking' in payload:
        return AccountLinking(payload)

    return


class Webhook(object):
    def __init__(self, payload):
        self.user_id = self.sender_id = payload['sender'].get('id')
        self.page_id = self.recipient_id = payload['recipient'].get('id')
        self.timestamp = payload.get('timestamp')
        """ :type dict """
        self.payload = payload

    def __str__(self):
        return str(self.payload)

    def __unicode__(self):
        return self.__str__()

    def __repr__(self):
        return str(self.__dict__)


class Authentication(Webhook):
    """
    :see https://developers.facebook.com/docs/messenger-platform/webhook-reference/authentication
    """
    type = webhook_types.AUTHENTICATION

    def __init__(self, payload):
        super(Authentication, self).__init__(payload)

        self.optin_ref = payload['optin'].get('ref')


class MessageReceived(Webhook):
    """
    :see https://developers.facebook.com/docs/messenger-platform/webhook-reference/message-received
    """
    type = webhook_types.MESSAGE_RECEIVED

    def __init__(self, payload):
        super(MessageReceived, self).__init__(payload)

        self.mid = payload['message'].get('mid')
        self.seq = payload['message'].get('seq')
        self.text = payload['message'].get('text')
        self.attachments = payload['message'].get('attachments')

        if 'quick_reply' in payload['message']:
            self.quick_reply_payload = payload['message']['quick_reply'].get('payload')
        else:
            self.quick_reply_payload = None


class MessageDelivered(Webhook):
    """
    :see https://developers.facebook.com/docs/messenger-platform/webhook-reference/message-delivered
    """
    type = webhook_types.MESSAGE_DELIVERED

    def __init__(self, payload):
        super(MessageDelivered, self).__init__(payload)

        self.seq = payload['delivery'].get('seq')
        self.watermark = payload['delivery'].get('watermark')
        self.mids = payload['delivery'].get('mids')


class MessageRead(Webhook):
    """
    :see https://developers.facebook.com/docs/messenger-platform/webhook-reference/message-read
    """
    type = webhook_types.MESSAGE_READ

    def __init__(self, payload):
        super(MessageRead, self).__init__(payload)

        self.seq = payload['read'].get('seq')
        self.watermark = payload['read'].get('watermark')


class Postback(Webhook):
    """
    :see https://developers.facebook.com/docs/messenger-platform/webhook-reference/postback-received
    """
    type = webhook_types.POSTBACK_RECEIVED

    def __init__(self, payload):
        super(Postback, self).__init__(payload)

        self.postback_payload = payload['postback'].get('payload')


class AccountLinking(Webhook):
    """
    :see https://developers.facebook.com/docs/messenger-platform/webhook-reference/account-linking
    """
    type = webhook_types.ACCOUNT_LINKING

    def __init__(self, payload):
        super(AccountLinking, self).__init__(payload)

        self.status = payload['account_linking'].get('status')
        self.authorization_code = payload['account_linking'].get('authorization_code')
