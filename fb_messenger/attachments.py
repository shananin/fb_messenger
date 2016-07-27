"""
Attachments collection
:see https://developers.facebook.com/docs/messenger-platform/send-api-reference
"""
from __future__ import unicode_literals

from .interfaces import IAttachment, ISubElement


class Text(IAttachment):
    """
    :see https://developers.facebook.com/docs/messenger-platform/send-api-reference/text-message
    """

    def __init__(self, text, quick_replies=None):
        """
        :type text: str
        :type quick_replies: list[QuickReply]
        """
        self.text = text
        self.quick_replies = quick_replies

    def to_dict(self):
        data = {
            'text': self.text,
        }

        if self.quick_replies:
            data['quick_replies'] = [quick_reply.to_dict() for quick_reply in self.quick_replies]

        return data


class QuickReply(ISubElement):
    """
    :see https://developers.facebook.com/docs/messenger-platform/send-api-reference/quick-replies
    """

    def __init__(self, title, payload, content_type='text'):
        """
        :type content_type: str
        :type payload: str
        :type title: str
        """
        self.title = title
        self.payload = payload
        self.content_type = content_type

    def to_dict(self):
        return {
            'content_type': self.content_type,
            'title': self.title,
            'payload': self.payload,
        }


class Image(IAttachment):
    """
    :see https://developers.facebook.com/docs/messenger-platform/send-api-reference/image-attachment
    """

    def __init__(self, image_url):
        """
        :type image_url: str
        """
        self.image_url = image_url

    def to_dict(self):
        return {
            'attachment': {
                'type': 'image',
                'payload': {
                    'url': self.image_url,
                },
            },
        }


class Buttons(IAttachment):
    """
    :see https://developers.facebook.com/docs/messenger-platform/send-api-reference/button-template
    """

    def __init__(self, text, buttons):
        """
        :type text: str
        :type buttons: list[ButtonWithWebUrl|ButtonWithPostback]
        """
        self.text = text
        self.buttons = buttons

    def to_dict(self):
        return {
            'attachment': {
                'type': 'template',
                'payload': {
                    'template_type': 'button',
                    'text': self.text,
                    'buttons': [button.to_dict() for button in self.buttons]
                },
            },
        }


class ButtonWithWebUrl(ISubElement):
    """
    :see https://developers.facebook.com/docs/messenger-platform/send-api-reference/button-template
    """

    def __init__(self, title, web_url):
        """
        :type title: str
        :type web_url: str
        """
        self.title = title
        self.web_url = web_url

    def to_dict(self):
        return {
            'type': 'web_url',
            'title': self.title,
            'url': self.web_url,
        }


class ButtonWithPostback(ISubElement):
    """
    :see https://developers.facebook.com/docs/messenger-platform/send-api-reference/button-template
    """

    def __init__(self, title, payload):
        """
        :type title: str
        :type payload: str
        """
        self.title = title
        self.payload = payload

    def to_dict(self):
        return {
            'type': 'postback',
            'title': self.title,
            'payload': self.payload,
        }


class GenericSubElement(ISubElement):
    """
    :see https://developers.facebook.com/docs/messenger-platform/send-api-reference/generic-template
    """

    def __init__(self, title, item_url=None, image_url=None, subtitle=None, buttons=None):
        """
        :type title: str
        :type item_url: str
        :type image_url: str
        :type subtitle: str
        :type buttons: list[ButtonWithWebUrl|ButtonWithPostback]
        """
        self.title = title
        self.item_url = item_url
        self.image_url = image_url
        self.subtitle = subtitle
        self.buttons = buttons

    def to_dict(self):
        data = {
            'title': self.title,
        }

        if self.item_url:
            data['item_url'] = self.item_url

        if self.image_url:
            data['image_url'] = self.image_url

        if self.subtitle:
            data['subtitle'] = self.subtitle

        if self.buttons:
            data['buttons'] = [button.to_dict() for button in self.buttons]

        return data


class Generic(IAttachment):
    """
    :see https://developers.facebook.com/docs/messenger-platform/send-api-reference/generic-template
    """

    def __init__(self, generic_sub_elements):
        """
        :type generic_sub_elements: list[GenericSubElement]
        """
        self.generic_sub_elements = generic_sub_elements

    def to_dict(self):
        return {
            'attachment': {
                'type': 'template',
                'payload': {
                    'template_type': 'generic',
                    'elements': [element.to_dict() for element in self.generic_sub_elements],
                },
            },
        }


class Receipt(IAttachment):
    """
    TODO: complete receipt attachment
    :see https://developers.facebook.com/docs/messenger-platform/send-api-reference/receipt-template
    """

    def __init__(self, recipient_name, order_number, currency, payment_method, receipt_sub_elements,
                 summary, timestamp=None, order_url=None, address=None, adjustments=None):
        """
        :type recipient_name: str
        :type order_number: str
        :type currency: str - 'USD', 'EUR'
        :type payment_method: str - 'Visa', 'MasterCard'
        :type receipt_sub_elements: list[ReceiptSubElement]
        :type summary: Summary
        """
        self.recipient_name = recipient_name
        self.order_number = order_number
        self.currency = currency
        self.payment_method = payment_method
        self.receipt_sub_elements = receipt_sub_elements
        self.summary = summary
        self.timestamp = timestamp
        self.order_url = order_url
        self.address = address
        self.adjustments = adjustments

    def to_dict(self):
        data = {
            'attachment': {
                'type': 'template',
                'payload': {
                    'template_type': 'receipt',
                    'recipient_name': self.recipient_name,
                    'order_number': self.order_number,
                    'currency': self.currency,
                    'payment_method': self.payment_method,
                    'elements': [element.to_dict() for element in self.receipt_sub_elements],
                    'summary': self.summary.to_dict(),
                },
            },
        }

        if self.timestamp:
            data['timestamp'] = self.timestamp

        if self.order_url:
            data['order_url'] = self.order_url

        if self.address:
            data['address'] = self.address.to_dict()

        if self.adjustments:
            data['adjustments'] = [elem.to_dict() for elem in self.adjustments]

        return data


class Summary(ISubElement):
    """
    :see https://developers.facebook.com/docs/messenger-platform/send-api-reference/receipt-template
    """

    def __init__(self, total_cost, subtotal=None, shipping_cost=None, total_tax=None):
        """
        :type total_cost: float|int
        :type subtotal: float|int
        :type shipping_cost: float|int
        :type total_tax: float|int
        """
        self.total_cost = total_cost
        self.subtotal = subtotal
        self.shipping_cost = shipping_cost
        self.total_tax = total_tax

    def to_dict(self):
        data = {
            'total_cost': self.total_cost,
        }

        if self.subtotal:
            data['subtotal'] = self.subtotal

        if self.shipping_cost:
            data['shipping_cost'] = self.shipping_cost

        if self.total_tax:
            data['total_tax'] = self.total_tax

        return data


class ReceiptSubElement(ISubElement):
    """
    :see https://developers.facebook.com/docs/messenger-platform/send-api-reference/receipt-template
    """

    def __init__(self, title, subtitle=None, quantity=None,
                 price=None, currency=None, image_url=None):
        """
        :type title: str
        :type subtitle: str
        :type quantity: int
        :type price: float|int
        :type currency: str
        :type image_url: str
        """
        self.title = title
        self.subtitle = subtitle
        self.quantity = quantity
        self.price = price
        self.currency = currency
        self.image_url = image_url

    def to_dict(self):
        data = {
            'title': self.title,
        }

        if self.subtitle:
            data['subtitle'] = self.subtitle

        if self.quantity:
            data['quantity'] = self.quantity

        if self.price:
            data['price'] = self.price

        if self.currency:
            data['currency'] = self.currency

        if self.image_url:
            data['image_url'] = self.image_url

        return data
