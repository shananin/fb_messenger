from __future__ import unicode_literals
import unittest
from  fb_messenger import attachments


# from fb_messenger.attachments import *
# from fb_messenger.exceptions import FBIncorrectType
#
#
# class ImageTest(unittest.TestCase):
#     def test_dict_with_valid_data(self):
#         url = 'http://example.com/image.png'
#         image = Image(url)
#
#         self.assertDictEqual(image.get_dict(), {
#             'type': 'image',
#             'payload': {
#                 'url': url
#             }
#         })
#
#     def test_error_on_invalid_data(self):
#         url = 5
#
#         with self.assertRaises(FBIncorrectType):
#             Image(url)

class FirstTest(unittest.TestCase):
    def first(self):
        self.assertEqual(True, True)
