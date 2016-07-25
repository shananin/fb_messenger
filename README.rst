Python API client for FB Messenger (under development)
======================================================

.. image:: https://travis-ci.org/shananin/fb_messenger.svg?branch=master
    :target: https://travis-ci.org/shananin/fb_messenger

.. image:: https://coveralls.io/repos/github/shananin/fb_messenger/badge.svg?branch=master
    :target: https://coveralls.io/github/shananin/fb_messenger?branch=master

Installation
~~~~~~~~~~~~

Minimum Requirements
____________________

-  Python 2.7+ or Python 3.3+

Install from pip
________________


.. code-block:: sh

    pip install fb_messenger

Build from source
_________________


.. code-block:: sh

    git clone https://github.com/shananin/fb_messenger
    cd fb_messenger
    python setup.py install

How to develop
______________

.. code-block:: sh

    make install # create virtualenv folder and install requirements
    make lint # run pylint
    make test # run tests
    make clean # remove virtualenv folder


How to Use
~~~~~~~~~~

Send simple text
________________

.. code-block:: python

    from fb_messenger.client import FBMessenger
    from fb_messenger import attachments
    from fb.messenger.exceptions import MessengerAPIError

    client = FBMessenger(ACCESS_TOKEN, logger_level=logging.DEBUG)
    text = attachments.Text('hello!')

    try:
        response = client.send_attachment(RECIPIENT_ID, text)
    except MessengerAPIError as e:
        LOGGER.debug(e)


Send attachment
_______________

More examples look into `examples` folder.


.. code-block:: python

    image = attachments.Image('http://example.com/img.jpg')

    try:
        response = client.send_attachment(RECIPIENT_ID, text)
    except MessengerAPIError as e:
        LOGGER.debug(e)


Send action
___________

.. code-block:: python

    from fb_messenger.types import action_types

    try:
        response = client.send_action(RECIPIENT_ID, action_types.MARK_SEEN)
    except MessengerAPIError as e:
        LOGGER.debug(e)


How to process messages in Flask
________________________________

.. code-block:: python

    from flask import Flask, request
    import logging
    from fb_messenger.client import FBMessenger
    from fb_messenger.types import webhook_types

    app = Flask(__name__)

    logging.basicConfig()
    LOGGER = logging.getLogger(__name__)
    LOGGER.setLevel(logging.DEBUG)

    client = FBMessenger(ACCESS_TOKEN, logger_level=logging.DEBUG)


    @app.route('/webhook', methods=['GET'])
    def get_webhook():
        if request.args.get('hub.verify_token', '') == VERIFY_TOKEN:
            return request.args.get('hub.challenge', '')

        return 'Error', 400


    @app.route('/webhook', methods=['POST'])
    def post_webhook():
        try:
            client.process_message(request.get_json())
        except Exception as e:
            LOGGER.debug(e)

        return 'ok'


    @client.register_webhook(webhook_types.MESSAGE_RECEIVED)
    def message_received(webhook):
        """
        :type webhook: fb_messenger.webhooks.MessageReceived
        """
        LOGGER.debug((webhook_types.MESSAGE_RECEIVED, webhook))


    @client.register_webhook(webhook_types.POSTBACK_RECEIVED)
    def postback_received(webhook):
        """
        :type webhook: fb_messenger.webhooks.Postback
        """
        LOGGER.debug((webhook_types.POSTBACK_RECEIVED, webhook))


    @client.register_webhook(webhook_types.AUTHENTICATION)
    def authentication(webhook):
        """
        :type webhook: fb_messenger.webhooks.Authentication
        """
        LOGGER.debug((webhook_types.AUTHENTICATION, webhook))


    @client.register_webhook(webhook_types.ACCOUNT_LINKING)
    def account_linking(webhook):
        """
        :type webhook: fb_messenger.webhooks.AccountLinking
        """
        LOGGER.debug((webhook_types.ACCOUNT_LINKING, webhook))


    @client.register_webhook(webhook_types.MESSAGE_DELIVERED)
    def message_delivered(webhook):
        """
        :type webhook: fb_messenger.webhooks.MessageDelivered
        """
        LOGGER.debug((webhook_types.MESSAGE_DELIVERED, webhook))


    @client.register_webhook(webhook_types.MESSAGE_READ)
    def message_read(webhook):
        """
        :type webhook: fb_messenger.webhooks.MessageRead
        """
        LOGGER.debug((webhook_types.MESSAGE_READ, webhook))


    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')

