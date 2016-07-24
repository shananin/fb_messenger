from __future__ import unicode_literals

success_send_action_response = {
    'recipient_id': '111',
}

success_send_attachment_response = {
    'recipient_id': '111',
    'message_id': 'mid.1469190965111:a229991ed7b8f01222'
}

failed_send_response = {
    'error': {
        'message': 'Invalid OAuth access token.',
        'type': 'OAuthException',
        'code': 190,
        'fbtrace_id': 'BLBz/WZt8dN'
    }
}

message_receive_text_webhook = {
    "sender": {
        "id": "USER_ID"
    },
    "recipient": {
        "id": "PAGE_ID"
    },
    "timestamp": 1458692752478,
    "message": {
        "mid": "mid.1457764197618:41d102a3e1ae206a38",
        "seq": 73,
        "text": "hello, world!",
        "quick_reply": {
            "payload": "DEVELOPER_DEFINED_PAYLOAD"
        }
    }
}

message_receive_attachments_webhook = {
    "sender": {
        "id": "USER_ID"
    },
    "recipient": {
        "id": "PAGE_ID"
    },
    "timestamp": 1458692752478,
    "message": {
        "mid": "mid.1458696618141:b4ef9d19ec21086067",
        "seq": 51,
        "attachments": [
            {
                "type": "image",
                "payload": {
                    "url": "IMAGE_URL"
                }
            }
        ]
    }
}

postback_webhook = {
    "sender": {
        "id": "USER_ID"
    },
    "recipient": {
        "id": "PAGE_ID"
    },
    "timestamp": 1458692752478,
    "postback": {
        "payload": "USER_DEFINED_PAYLOAD"
    }
}

authentication_webhook = {
    "sender": {
        "id": "USER_ID"
    },
    "recipient": {
        "id": "PAGE_ID"
    },
    "timestamp": 1234567890,
    "optin": {
        "ref": "PASS_THROUGH_PARAM"
    }
}

account_linking_linked_webhook = {
    "sender": {
        "id": "USER_ID"
    },
    "recipient": {
        "id": "PAGE_ID"
    },
    "timestamp": 1234567890,
    "account_linking": {
        "status": "linked",
        "authorization_code": "PASS_THROUGH_AUTHORIZATION_CODE"
    }
}

account_linking_unlinked_webhook = {
    "sender": {
        "id": "USER_ID"
    },
    "recipient": {
        "id": "PAGE_ID"
    },
    "timestamp": 1234567890,
    "account_linking": {
        "status": "unlinked"
    }
}

message_delivered_webhook = {
    "sender": {
        "id": "USER_ID"
    },
    "recipient": {
        "id": "PAGE_ID"
    },
    "delivery": {
        "mids": [
            "mid.1458668856218:ed81099e15d3f4f233"
        ],
        "watermark": 1458668856253,
        "seq": 37
    }
}

message_read_webhook = {
    "sender": {
        "id": "USER_ID"
    },
    "recipient": {
        "id": "PAGE_ID"
    },
    "timestamp": 1458668856463,
    "read": {
        "watermark": 1458668856253,
        "seq": 38
    }
}

message_hello_full_webhook = {'entry': [{'messaging': [
    {'recipient': {'id': '1579236102311111'}, 'sender': {'id': '1447507518611111'},
     'message': {'mid': 'mid.1469347911111:4128b8d2be11115554', 'text': 'hello', 'seq': 56},
     'timestamp': 1469347944638}], 'time': 1469347944663, 'id': '1579236102311112'}], 'object': 'page'}


response_message_send = {
    'recipient_id': '1111507518611111',
    'message_id': 'mid.1119349798111:111d5035d88d474111'
}

response_action_send = {
    'recipient_id': '1111507518611111',
}

# TODO: Message echo
