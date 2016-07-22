from __future__ import unicode_literals
from fb_messenger.fb_messenger import attachments


def test_text():
    text = 'test text'

    assert attachments.Text(text=text).to_dict() == {
        'text': text,
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


def test_generic_element():
    title = 'generic_title'
    item_url = 'http://example.com/'
    image_url = 'http://example.com/img.jpg'
    subtitle = 'subtitle'
    buttons = None

    assert attachments.GenericElement(title).to_dict() == {
        'title': title
    }

    assert attachments.GenericElement(title, item_url=item_url).to_dict() == {
        'title': title,
        'item_url': item_url,
    }

    assert attachments.GenericElement(title=title, item_url=item_url, image_url=image_url).to_dict() == {
        'title': title,
        'item_url': item_url,
        'image_url': image_url,
    }

    assert attachments.GenericElement(
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
