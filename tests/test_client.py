from __future__ import unicode_literals
import pytest
from mock import MagicMock
from fb_messenger.fb_messenger.client import FBMessenger, Response
from fb_messenger.fb_messenger.types import action_types
from fb_messenger.fb_messenger import exceptions


def test_send_action():
    client = FBMessenger(access_token='test')

    response_dict = {
        'recipient_id': '111',
    }

    client._send_request = MagicMock(
        return_value=response_dict
    )

    assert client.send_action('111', action_types.MARK_SEEN) == Response(response_dict)
    assert client.send_action('111', action_types.TYPING_OFF) == Response(response_dict)
    assert client.send_action('111', action_types.TYPING_ON) == Response(response_dict)

    with pytest.raises(exceptions.UnknownAction):
        client.send_action('111', 'test')
