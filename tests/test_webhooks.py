from __future__ import unicode_literals
from . import data
from fb_messenger.fb_messenger import webhooks


def test_authentication_webhook():
    payload = data.authentication_webhook
    auth_webhook = webhooks.Authentication(payload)

    assert auth_webhook.recipient_id == payload['recipient']['id']
    assert auth_webhook.sender_id == payload['sender']['id']
    assert auth_webhook.timestamp == payload['timestamp']
    assert auth_webhook.optin_ref == payload['optin']['ref']
    assert auth_webhook.payload == payload


def test_message_delivered_webhook():
    payload = data.message_delivered_webhook
    message_delivered = webhooks.MessageDelivered(payload)

    assert message_delivered.recipient_id == payload['recipient']['id']
    assert message_delivered.sender_id == payload['sender']['id']
    assert message_delivered.delivery_mids == payload['delivery']['mids']
    assert message_delivered.delivery_seq == payload['delivery']['seq']
    assert message_delivered.delivery_watermark == payload['delivery']['watermark']
    assert message_delivered.payload == payload


def test_message_read_webhook():
    payload = data.message_read_webhook
    message_read = webhooks.MessageRead(payload)

    assert message_read.recipient_id == payload['recipient']['id']
    assert message_read.sender_id == payload['sender']['id']
    assert message_read.timestamp == payload['timestamp']
    assert message_read.read_watermark == payload['read']['watermark']
    assert message_read.read_seq == payload['read']['seq']
    assert message_read.payload == payload


def test_postback_webhook():
    payload = data.postback_webhook
    postback = webhooks.Postback(payload)

    assert postback.recipient_id == payload['recipient']['id']
    assert postback.sender_id == payload['sender']['id']
    assert postback.timestamp == payload['timestamp']
    assert postback.postback_payload == payload['postback']['payload']
    assert postback.payload == payload


def test_account_linking_webhook():
    payload = data.account_linking_linked_webhook
    account_linking_linked = webhooks.AccountLinking(payload)

    assert account_linking_linked.recipient_id == payload['recipient']['id']
    assert account_linking_linked.sender_id == payload['sender']['id']
    assert account_linking_linked.timestamp == payload['timestamp']
    assert account_linking_linked.account_linking_status == payload['account_linking']['status']
    assert account_linking_linked.account_linking_authorization_code == payload['account_linking']['authorization_code']
    assert account_linking_linked.payload == payload

    payload = data.account_linking_unlinked_webhook
    account_linking_unlinked = webhooks.AccountLinking(payload)

    assert account_linking_unlinked.recipient_id == payload['recipient']['id']
    assert account_linking_unlinked.sender_id == payload['sender']['id']
    assert account_linking_unlinked.timestamp == payload['timestamp']
    assert account_linking_unlinked.account_linking_status == payload['account_linking']['status']
    assert account_linking_unlinked.account_linking_authorization_code is None
    assert account_linking_unlinked.payload == payload


def test_message_received_webhook():
    payload = data.message_receive_text_webhook
    message_received = webhooks.MessageReceived(payload)

    assert message_received.recipient_id == payload['recipient']['id']
    assert message_received.sender_id == payload['sender']['id']
    assert message_received.timestamp == payload['timestamp']
    assert message_received.mid == payload['message']['mid']
    assert message_received.seq == payload['message']['seq']
    assert message_received.text == data.message_receive_text_webhook['message']['text']
    assert message_received.payload == payload


def test_parse():
    assert isinstance(webhooks.parse_payload(data.authentication_webhook), webhooks.Authentication)
    assert isinstance(webhooks.parse_payload(data.message_receive_text_webhook), webhooks.MessageReceived)
    assert isinstance(webhooks.parse_payload(data.message_delivered_webhook), webhooks.MessageDelivered)
    assert isinstance(webhooks.parse_payload(data.message_read_webhook), webhooks.MessageRead)
    assert isinstance(webhooks.parse_payload(data.account_linking_linked_webhook), webhooks.AccountLinking)
    assert isinstance(webhooks.parse_payload(data.postback_webhook), webhooks.Postback)
    assert webhooks.parse_payload({}) is None
