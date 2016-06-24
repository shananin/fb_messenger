import unittest

from fb_messenger.message import Message


class SecondTest(unittest.TestCase):
    def test_second(self):
        message = Message('111', text='111')

        self.assertEqual({
            'recipient': {
                'id': '111',
            },
            'message': {
                'text': '111'
            },
            'notification_type': 'REGULAR',
        }, message.get_dict(), 'Message error')
