import json
from .exceptions import IncorrectFBRequest, UnknownCallback


class CallbacksParser(object):
    def __init__(self, body):
        if type(body) is str:
            body = json.loads(body)

        self.body = body

    def parse(self):
        parsed_requests = []

        if 'entry' not in self.body:
            raise IncorrectFBRequest

        for entry in self.body['entry']:
            if 'messaging' not in entry:
                raise IncorrectFBRequest

            for message in entry['messaging']:
                callbacks_factory = CallbacksFactory(message)
                parsed_requests.append(callbacks_factory.get_callback())

        return parsed_requests


class CallbacksFactory(object):
    def __init__(self, message):
        self.message = message

    def get_callback(self):
        if 'message' in self.message:
            return MessageReceived(self.message)

        if 'delivery' in self.message:
            return MessageDelivery(self.message)

        if 'postback' in self.message:
            return Postback(self.message)

        if 'optin' in self.message:
            return Authentication(self.message)

        raise UnknownCallback


class Callback(object):
    def __init__(self, message):
        if ('sender' or 'recipient') not in message:
            raise IncorrectFBRequest

        self.user_id = self.sender_id = message['sender']['id']
        self.page_id = self.recipient_id = message['recipient']['id']


class Authentication(Callback):
    def __init__(self, message):
        super(Authentication, self).__init__(message)

        if ('optin' or 'timestamp') not in message:
            raise IncorrectFBRequest

        self.timestamp = message['timestamp']

        if 'ref' not in message['optin']:
            raise IncorrectFBRequest

        self.ref = message['optin']['ref']


class MessageReceived(Callback):
    text = None
    attachments = None

    def __init__(self, message):
        super(MessageReceived, self).__init__(message)

        if ('mid' or 'seq') not in message['message']:
            raise IncorrectFBRequest

        self.mid = message['message']['mid']
        self.seq = message['message']['seq']

        if 'text' in message['message']:
            self.text = message['message']['text']

        if 'attachments' in message['message']:
            attachments = []
            for attachment in message['message']['attachments']:
                if 'type' not in attachment:
                    continue

                if attachment['type'] == 'image':
                    attachments.append(ImageReceive(attachment))
                elif attachment['type'] == 'location':
                    attachments.append(LocationReceive(attachment))

            self.attachments = attachments


class MessageDelivery(Callback):
    mids = None

    def __init__(self, message):
        super(MessageDelivery, self).__init__(message)

        if ('seq' or 'watermark') not in message['delivery']:
            raise IncorrectFBRequest

        self.seq = message['delivery']['seq']
        self.watermark = message['delivery']['watermark']

        if 'mids' in message['delivery']:
            self.mids = message['delivery']['mids']


class Postback(Callback):
    def __init__(self, message):
        super(Postback, self).__init__(message)

        if ('postback' or 'timestamp') not in message:
            raise IncorrectFBRequest

        self.timestamp = message['timestamp']

        if 'payload' not in message['postback']:
            raise IncorrectFBRequest

        self.payload = message['postback']['payload']


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
