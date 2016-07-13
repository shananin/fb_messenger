from __future__ import unicode_literals
from fb_messenger import (
    utils,
    attachments,
    notification_type as nt
)


def test_get_dict_for_message():
    recipient_id = '13123131343'
    title = 'button_title'
    url = 'http://example.com'
    notification_type = nt.REGULAR

    attachment = attachments.ButtonWithWebUrl(title, url)
    assert utils.get_dict_for_message(
        recipient_id,
        attachment,
        notification_type,
    ) == {
        'message': {
            'attachment': attachment.to_dict()
        },
        'notification_type': notification_type,
        'recipient': {
            'id': recipient_id
        }
    }
