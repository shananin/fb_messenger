from interfaces import IButton


class ButtonWithWebUrl(IButton):
    def __init__(self, title, web_url):
        self.title = title
        self.web_url = web_url

    def get_dict(self):
        return {
            'type': 'web_url',
            'title': self.title,
            'url': self.web_url,
        }


class ButtonWithPostback(IButton):
    def __init__(self, title, payload):
        self.title = title
        self.payload = payload

    def get_dict(self):
        return {
            'type': 'postback',
            'title': self.title,
            'payload': self.payload,
        }
