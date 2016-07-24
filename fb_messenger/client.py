"""
client = FBMessenger(access_token='ADSD...')

    try:
        response = client.send_text('1231313', 'text')
    except MainException as e:
        logging.debug(e)

    attachment = attachments.Image(img_url='http://example.com/img.jpg')
    try:
        response = client.send_attachment('1231313', attachment)
    except MainException as e:
        logging.debug(e)

"""
from __future__ import unicode_literals
import logging
import requests
from .types import (
    action_types,
    webhook_types,
    notification_types,
)
from . import const
from .exceptions import UnknownAction, MessengerAPIError, UnknownNotificationType, InvalidBody
from .interfaces import IFBPayload
from .webhooks import parse_payload


class FBMessenger(object):
    _webhooks = {}

    def __init__(self, access_token, logger=None, logger_level=None):
        if logger is not None:
            self.logger = logger
        else:
            logging.basicConfig()
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.WARNING)

        if logger_level is not None:
            self.logger.setLevel(logger_level)

        self._access_token = access_token
        self._api_url = const.API_FB_MESSAGES_URL + self._access_token

    def send_attachment(self, recipient_id, attachment, notification_type=notification_types.REGULAR):
        if notification_type not in notification_types.ALL_NOTIFICATION_TYPES:
            raise UnknownNotificationType

        if isinstance(attachment, IFBPayload):
            payload = _format_attachment_payload(recipient_id, attachment.to_dict(), notification_type)
        else:
            raise TypeError

        return Response(self._send_request(payload))

    def send_action(self, recipient_id, sender_action):
        """
        Set typing indicators or send read receipts using the Send API,
        to let users know you are processing their request.


        :param recipient_id: user id
        :param sender_action: look fb_messenger.action_types
        :return Response:
        """
        if sender_action not in action_types.ALL_ACTIONS:
            raise UnknownAction

        response_dict = self._send_request(
            _format_action_payload(recipient_id, sender_action)
        )

        return Response(response_dict)

    def process_message(self, body):
        self.logger.debug(body)
        if 'entry' not in body:
            raise InvalidBody

        for entry in body['entry']:
            if 'messaging' not in entry:
                continue

            for messaging in entry['messaging']:
                webhook = parse_payload(messaging)

                if not webhook:
                    continue

                if webhook.type in self._webhooks:
                    self._webhooks[webhook.type](webhook)

    def register_webhook(self, webhook_type):
        def decorator(function):
            if webhook_type not in webhook_types.ALL_WEBHOOKS:
                self.logger.warn('{} is not fb messenger callback'.format(webhook_type))
                return function

            self.logger.info('{} callback has been added'.format(webhook_type))
            self._webhooks[webhook_type] = function
            return function

        return decorator

    def create_welcome_message(self, page_id, message):
        payload = _format_welcome_message(message)

        request = requests.post(
            url='https://graph.facebook.com/v2.6/{}/thread_settings?access_token={}'.format(page_id,
                                                                                            self._access_token),
            json=payload,
        )

        return request.status_code, request.json()

    def _send_request(self, payload):
        request = requests.post(
            url=self._api_url,
            json=payload,
        )

        response_dict = request.json()

        if request.status_code >= 300:
            raise MessengerAPIError(response_dict)

        return response_dict


class Response(object):
    def __init__(self, response_dict):
        self.recipient_id = response_dict.get('recipient_id')
        self.message_id = response_dict.get('message_id')
        self.response_dict = response_dict

    def __str__(self):
        return str(self.response_dict)

    def __unicode__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.response_dict == other.response_dict


def _format_action_payload(recipient_id, sender_action):
    return {
        'recipient': {
            'id': recipient_id,
        },
        'sender_action': sender_action,
    }


def _format_attachment_payload(recipient_id, attachment, notification_type):
    return {
        'recipient': {
            'id': recipient_id,
        },
        'message': attachment,
        'notification_type': notification_type,
    }


def _format_welcome_message(attachment):
    return {
        'setting_type': 'call_to_actions',
        'thread_state': 'new_thread',
        'call_to_actions': [
            {
                'message': {
                    attachment
                }
            },
        ],
    }
