import json


class Response(object):
    recipient_id = None
    message_id = None

    def __init__(self, response):
        if type(response) is str:
            response = json.loads(response)

        self.response = response

    def parse(self):
        self.recipient_id = self.response['recipient_id']
        self.message_id = self.response['message_id']
        return self
