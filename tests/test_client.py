from __future__ import unicode_literals
import json
import pytest
import requests_mock
from fb_messenger.fb_messenger.client import FBMessenger, Response
from fb_messenger.fb_messenger.types import action_types
from fb_messenger.fb_messenger import exceptions
from . import data


@requests_mock.Mocker()
def test_send_action(m):
    client = FBMessenger(access_token='test')

    m.post(client._api_url, text=json.dumps(data.success_send_action_response))

    assert client.send_action('111', action_types.MARK_SEEN) == Response(data.success_send_action_response)
    assert client.send_action('111', action_types.TYPING_OFF) == Response(data.success_send_action_response)
    assert client.send_action('111', action_types.TYPING_ON) == Response(data.success_send_action_response)

    with pytest.raises(exceptions.UnknownAction):
        client.send_action('111', 'test')


@requests_mock.Mocker()
def test_failed_send_action(m):
    client = FBMessenger(access_token='test')

    m.post(client._api_url, text=json.dumps(data.failed_send_response), status_code=400)

    # check exception after failed requests
    with pytest.raises(exceptions.MessengerAPIError):
        client.send_action('111', action_types.TYPING_ON)

    # check error parsing
    try:
        client.send_action('111', action_types.TYPING_ON)
    except exceptions.MessengerAPIError as e:
        assert e.message == data.failed_send_response['error']['message']
        assert e.type == data.failed_send_response['error']['type']
        assert e.code == data.failed_send_response['error']['code']
        assert e.fbtrace_id == data.failed_send_response['error']['fbtrace_id']
