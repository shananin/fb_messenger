import notification_type as nt
from interfaces import IFBPayload


class Message(object):
    def __init__(self, recipient, text=None, attachment=None, notification_type=nt.REGULAR):
        self.recipient = recipient
        self.text = text
        self.attachment = attachment
        self.notification_type = notification_type

    def get_dict(self):
        data = {
            'recipient': {
                'id': self.recipient,
            },
            'message': {},
            'notification_type': self.notification_type,
        }

        if type(self.text) is str or type(self.text) is unicode:
            data['message']['text'] = self.text

        if type(self.attachment) is str or type(self.attachment) is unicode:
            data['message']['text'] = self.attachment

        if isinstance(self.attachment, IFBPayload):
            data['message']['attachment'] = self.attachment.get_dict()

        if isinstance(self.text, IFBPayload):
            data['message']['attachment'] = self.text.get_dict()

        return data
