"""
Callbacks parser
"""
from __future__ import unicode_literals
import json
from six import string_types
from .exceptions import RequestFailed, UnknownCallback
from .types import webhook_types


def parse(payload):
    pass


# class CallbacksParser(object):
#     def __init__(self, body):
#         if isinstance(body, string_types):
#             body = json.loads(body)
#
#         self.body = body
#
#     def parse(self):
#         parsed_requests = []
#
#         if 'entry' not in self.body:
#             raise RequestFailed
#
#         for entry in self.body['entry']:
#             if 'messaging' not in entry:
#                 raise RequestFailed
#
#             for message in entry['messaging']:
#                 callbacks_factory = CallbacksFactory(message)
#                 parsed_requests.append(callbacks_factory.get_callback())
#
#         return parsed_requests
#
#
# class CallbacksFactory(object):
#     def __init__(self, message):
#         self.message = message
#
#     def get_callback(self):
#         if 'message' in self.message:
#             return MessageReceived(self.message)
#
#         if 'delivery' in self.message:
#             return MessageDelivery(self.message)
#
#         if 'postback' in self.message:
#             return Postback(self.message)
#
#         if 'optin' in self.message:
#             return Authentication(self.message)
#
#         raise UnknownCallback


class Webhook(object):
    def __init__(self, payload):
        if ('sender' or 'recipient') not in payload:
            raise RequestFailed

        self.user_id = self.sender_id = payload['sender']['id']
        self.page_id = self.recipient_id = payload['recipient']['id']
        self.payload = payload


class Authentication(Webhook):
    def __init__(self, payload):
        super(Authentication, self).__init__(payload)

        if ('optin' or 'timestamp') not in payload:
            raise RequestFailed

        self.timestamp = payload['timestamp']

        if 'ref' not in payload['optin']:
            raise RequestFailed

        self.ref = payload['optin']['ref']


class MessageReceived(Webhook):
    text = None
    attachments = None

    def __init__(self, payload):
        super(MessageReceived, self).__init__(payload)

        if ('mid' or 'seq') not in payload['message']:
            raise RequestFailed

        self.mid = payload['message']['mid']
        self.seq = payload['message']['seq']

        if 'text' in payload['message']:
            self.text = payload['message']['text']

        if 'attachments' in payload['message']:
            attachments = []
            for attachment in payload['message']['attachments']:
                if 'type' not in attachment:
                    continue

                if attachment['type'] == 'image':
                    attachments.append(ImageReceive(attachment))
                elif attachment['type'] == 'location':
                    attachments.append(LocationReceive(attachment))

            self.attachments = attachments


class MessageDelivery(Webhook):
    mids = None

    def __init__(self, payload):
        super(MessageDelivery, self).__init__(payload)

        if ('seq' or 'watermark') not in payload['delivery']:
            raise RequestFailed

        self.seq = payload['delivery']['seq']
        self.watermark = payload['delivery']['watermark']

        if 'mids' in payload['delivery']:
            self.mids = payload['delivery']['mids']


class Postback(Webhook):
    def __init__(self, payload):
        super(Postback, self).__init__(payload)

        if ('postback' or 'timestamp') not in payload:
            raise RequestFailed

        self.timestamp = payload['timestamp']

        if 'payload' not in payload['postback']:
            raise RequestFailed

        self.payload = payload['postback']['payload']


class ImageReceive(object):
    def __init__(self, attachment):
        self.attachment = attachment


class LocationReceive(object):
    longitude = None
    latitude = None
    url = None

    def __init__(self, attachment):
        self.attachment = attachment
        if 'url' in attachment:
            self.url = attachment['url']

        if 'payload' not in attachment:
            return

        if 'coordinates' not in attachment['payload']:
            return

        self.longitude = attachment['payload']['coordinates']['long']
        self.latitude = attachment['payload']['coordinates']['lat']
