"""
Callbacks parser
"""
from __future__ import unicode_literals
from .exceptions import RequestFailed
from .types import webhook_types


def parse_payload(payload):
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
        if ('sender' or 'recipient') not in payload:
            raise RequestFailed

        self.user_id = self.sender_id = payload['sender'].get('id')
        self.page_id = self.recipient_id = payload['recipient'].get('id')
        self.timestamp = payload.get('timestamp')
        """ :type dict """
        self.payload = payload

    def __str__(self):
        return str(self.payload)

    def __unicode__(self):
        return self.__str__()


class Authentication(Webhook):
    type = webhook_types.AUTHENTICATION

    def __init__(self, payload):
        super(Authentication, self).__init__(payload)

        if ('optin' or 'timestamp') not in payload:
            raise RequestFailed

        self.timestamp = payload['timestamp']

        if 'ref' not in payload['optin']:
            raise RequestFailed

        self.optin_ref = payload['optin']['ref']


class MessageReceived(Webhook):
    type = webhook_types.MESSAGE_RECEIVED

    def __init__(self, payload):
        super(MessageReceived, self).__init__(payload)

        if ('mid' or 'seq') not in payload['message']:
            raise RequestFailed

        self.mid = payload['message']['mid']
        self.seq = payload['message']['seq']

        if 'text' in payload['message']:
            self.text = payload['message']['text']

        self.timestamp = payload.get('timestamp')

        if 'quick_reply' in payload['message']:
            self.quick_reply_payload = payload['message']['quick_reply']['payload']

        if 'attachments' in payload['message']:
            self.attachments = payload['message']['attachments']


class MessageDelivered(Webhook):
    type = webhook_types.MESSAGE_DELIVERED

    def __init__(self, payload):
        super(MessageDelivered, self).__init__(payload)

        if ('seq' or 'watermark') not in payload['delivery']:
            raise RequestFailed

        self.delivery_seq = payload['delivery']['seq']
        self.delivery_watermark = payload['delivery']['watermark']

        if 'mids' in payload['delivery']:
            self.delivery_mids = payload['delivery']['mids']


class MessageRead(Webhook):
    type = webhook_types.MESSAGE_READ

    def __init__(self, payload):
        super(MessageRead, self).__init__(payload)

        self.timestamp = payload.get('timestamp', None)

        if ('seq' or 'watermark') not in payload['read']:
            raise RequestFailed

        self.read_seq = payload['read']['seq']
        self.read_watermark = payload['read']['watermark']


class Postback(Webhook):
    type = webhook_types.POSTBACK_RECEIVED

    def __init__(self, payload):
        super(Postback, self).__init__(payload)

        if ('postback' or 'timestamp') not in payload:
            raise RequestFailed

        self.timestamp = payload['timestamp']

        if 'payload' not in payload['postback']:
            raise RequestFailed

        self.postback_payload = payload['postback']['payload']


class AccountLinking(Webhook):
    type = webhook_types.ACCOUNT_LINKING

    def __init__(self, payload):
        super(AccountLinking, self).__init__(payload)

        self.timestamp = payload.get('timestamp')

        self.account_linking_status = payload['account_linking'].get('status')
        self.account_linking_authorization_code = payload['account_linking'].get('authorization_code')
