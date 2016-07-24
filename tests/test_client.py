from __future__ import unicode_literals
import json
import pytest
import requests_mock
from fb_messenger.fb_messenger.client import (
    FBMessenger,
    Response,
    _format_action_payload,
    _format_attachment_payload,
)
from fb_messenger.fb_messenger.types import action_types, notification_types, webhook_types
from fb_messenger.fb_messenger import exceptions
from fb_messenger.fb_messenger import attachments
from . import data


def test_send_action():
    with requests_mock.Mocker() as m:
        client = FBMessenger(access_token='test')

        m.post(client._api_url, text=json.dumps(data.success_send_action_response))

        assert client.send_action('111', action_types.MARK_SEEN) == Response(data.success_send_action_response)
        assert client.send_action('111', action_types.TYPING_OFF) == Response(data.success_send_action_response)
        assert client.send_action('111', action_types.TYPING_ON) == Response(data.success_send_action_response)

        with pytest.raises(exceptions.UnknownAction):
            client.send_action('111', 'test')


def test_failed_send_action():
    with requests_mock.Mocker() as m:
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


def test_format_action_payload():
    recipient_id = '111'

    assert _format_action_payload(
        recipient_id, action_types.TYPING_ON
    ) == {
               'recipient': {
                   'id': recipient_id,
               },
               'sender_action': action_types.TYPING_ON,
           }


def test_format_attachment_payload():
    recipient_id = '111'
    attachment = attachments.Text('hello')

    assert _format_attachment_payload(
        recipient_id, attachment.to_dict(), notification_types.REGULAR
    ) == {
               'recipient': {
                   'id': recipient_id,
               },
               'message': attachment.to_dict(),
               'notification_type': notification_types.REGULAR,
           }


def test_process_hello():
    client = FBMessenger(access_token='test')

    @client.register_webhook(webhook_types.MESSAGE_RECEIVED)
    def process_received(webhook):
        assert webhook.payload == {
            'message': {'mid': 'mid.1469347911111:4128b8d2be11115554',
                         'seq': 56,
                         'text': 'hello'},
            'recipient': {'id': '1579236102311111'},
            'sender': {'id': '1447507518611111'},
            'timestamp': 1469347944638}

    client.process_message(data.message_hello_full_webhook)
