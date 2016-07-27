from __future__ import unicode_literals

from fb_messenger import attachments


def test_text():
    text = 'test text'

    assert attachments.Text(text=text).to_dict() == {
        'text': text,
    }

    title1 = 'title1'
    payload1 = 'payload1'
    quick_reply1 = attachments.QuickReply(title1, payload1)

    title2 = 'title2'
    payload2 = 'payload2'
    quick_reply2 = attachments.QuickReply(title2, payload2)

    assert attachments.Text(text, quick_replies=[quick_reply1, quick_reply2]).to_dict() == {
        'text': text,
        'quick_replies': [
            {
                'content_type': 'text',
                'title': title1,
                'payload': payload1,
            },
            {
                'content_type': 'text',
                'title': title2,
                'payload': payload2,
            },
        ],
    }


def test_image():
    img_url = 'http://example.com/img.jpg'

    assert attachments.Image(img_url).to_dict() == {
        'attachment': {
            'type': 'image',
            'payload': {
                'url': img_url,
            },
        }
    }


def test_button_with_web_url():
    title = 'button_title'
    url = 'http://example.com'

    assert attachments.ButtonWithWebUrl(title, url).to_dict() == {
        'type': 'web_url',
        'title': title,
        'url': url,
    }


def test_button_with_postback():
    title = 'button_title2'
    payload = 'test_payload'

    assert attachments.ButtonWithPostback(title, payload).to_dict() == {
        'type': 'postback',
        'title': title,
        'payload': payload,
    }


def test_buttons():
    title = 'title'

    title1 = 'button_title'
    url1 = 'http://example.com'
    button1 = attachments.ButtonWithWebUrl(title1, url1)

    title2 = 'button_title2'
    payload2 = 'test_payload'
    button2 = attachments.ButtonWithPostback(title2, payload2)

    assert attachments.Buttons(title, buttons=(button1, button2)).to_dict() == {
        'attachment': {
            'type': 'template',
            'payload': {
                'template_type': 'button',
                'text': title,
                'buttons': [
                    {
                        'type': 'web_url',
                        'title': title1,
                        'url': url1,
                    },
                    {
                        'type': 'postback',
                        'title': title2,
                        'payload': payload2,
                    },
                ],
            },
        },
    }


def test_generic_element():
    title = 'generic_title'
    item_url = 'http://example.com/'
    image_url = 'http://example.com/img.jpg'
    subtitle = 'subtitle'

    title1 = 'button_title'
    url1 = 'http://example.com'
    button1 = attachments.ButtonWithWebUrl(title1, url1)

    title2 = 'button_title2'
    payload2 = 'test_payload'
    button2 = attachments.ButtonWithPostback(title2, payload2)

    assert attachments.GenericItem(title).to_dict() == {
        'title': title
    }

    assert attachments.GenericItem(title, item_url=item_url).to_dict() == {
        'title': title,
        'item_url': item_url,
    }

    assert attachments.GenericItem(title=title, item_url=item_url, image_url=image_url).to_dict() == {
        'title': title,
        'item_url': item_url,
        'image_url': image_url,
    }

    assert attachments.GenericItem(
        title=title,
        item_url=item_url,
        image_url=image_url,
        subtitle=subtitle,
    ).to_dict() == {
               'title': title,
               'item_url': item_url,
               'image_url': image_url,
               'subtitle': subtitle,
           }

    assert attachments.GenericItem(
        title=title,
        item_url=item_url,
        image_url=image_url,
        subtitle=subtitle,
        buttons=[button1, button2],
    ).to_dict() == {
               'title': title,
               'item_url': item_url,
               'image_url': image_url,
               'subtitle': subtitle,
               'buttons': [
                   {
                       'type': 'web_url',
                       'title': title1,
                       'url': url1,
                   },
                   {
                       'type': 'postback',
                       'title': title2,
                       'payload': payload2,
                   },
               ],
           }


def test_generic():
    title1 = 'generic_elem_title1'
    generic_elem1 = attachments.GenericItem(title1)

    title2 = 'generic_elem_title2'
    generic_elem2 = attachments.GenericItem(title2)

    assert attachments.Generic([generic_elem1, generic_elem2]).to_dict() == {
        'attachment': {
            'type': 'template',
            'payload': {
                'template_type': 'generic',
                'elements': [
                    {
                        'title': title1
                    },
                    {
                        'title': title2
                    },
                ],
            },
        },
    }


def test_summary():
    total_cost = 26.00
    subtotal = 18.00
    shipping_cost = 5.00
    total_tax = 3.00

    assert attachments.Summary(total_cost).to_dict() == {
        'total_cost': total_cost,
    }

    assert attachments.Summary(total_cost, subtotal).to_dict() == {
        'total_cost': total_cost,
        'subtotal': subtotal,
    }

    assert attachments.Summary(total_cost, subtotal, shipping_cost).to_dict() == {
        'total_cost': total_cost,
        'subtotal': subtotal,
        'shipping_cost': shipping_cost,
    }

    assert attachments.Summary(total_cost, subtotal, shipping_cost, total_tax).to_dict() == {
        'total_cost': total_cost,
        'subtotal': subtotal,
        'shipping_cost': shipping_cost,
        'total_tax': total_tax,
    }


def test_receipt_element():
    title = 'title'
    subtitle = 'subtitle'
    quantity = 2
    price = 14.00
    currency = 'USD'
    image_url = 'http://example.com/img.jpg'

    assert attachments.ReceiptElement(title).to_dict() == {
        'title': title,
    }

    assert attachments.ReceiptElement(title, subtitle).to_dict() == {
        'title': title,
        'subtitle': subtitle,
    }

    assert attachments.ReceiptElement(title, subtitle, quantity).to_dict() == {
        'title': title,
        'subtitle': subtitle,
        'quantity': quantity,
    }

    assert attachments.ReceiptElement(title, subtitle, quantity, price).to_dict() == {
        'title': title,
        'subtitle': subtitle,
        'quantity': quantity,
        'price': price,
    }

    assert attachments.ReceiptElement(title, subtitle, quantity, price, currency).to_dict() == {
        'title': title,
        'subtitle': subtitle,
        'quantity': quantity,
        'price': price,
        'currency': currency,
    }

    assert attachments.ReceiptElement(title, subtitle, quantity, price, currency, image_url).to_dict() == {
        'title': title,
        'subtitle': subtitle,
        'quantity': quantity,
        'price': price,
        'currency': currency,
        'image_url': image_url,
    }


def test_receipe():
    recipient_name = 'recipient_name'
    order_number = '#434323'
    currency = 'USD'
    payment_method = 'Visa'
    elem_title = 'elem_title'
    elements = [attachments.ReceiptElement(elem_title)]
    summary = attachments.Summary(26.00)

    assert attachments.Receipt(
        recipient_name,
        order_number,
        currency,
        payment_method,
        elements,
        summary
    ).to_dict() == {
               'attachment': {
                   'type': 'template',
                   'payload': {
                       'template_type': 'receipt',
                       'recipient_name': recipient_name,
                       'order_number': order_number,
                       'currency': currency,
                       'payment_method': payment_method,
                       'elements': [
                           {
                               'title': elem_title,
                           },
                       ],
                       'summary': summary.to_dict(),
                   },
               },
           }
