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


How to Use
__________


.. code-block:: sh

    from flask import Flask, request
    import logging
    from fb_messenger.client import FBMessenger
    from fb_messenger.types import webhook_types

    app = Flask(__name__)
    client = FBMessenger(ACCESS_TOKEN, logger_level=logging.DEBUG)


    @app.route('/webhook', methods=['GET'])
    def get():
        logging.debug(request.args)
        if request.args.get('hub.verify_token', '') == VERIFY_TOKEN:
            logging.debug(request.args.get('hub.challenge', ''))
            return request.args.get('hub.challenge', '')

        return 'Error', 400


    @app.route('/webhook', methods=['POST'])
    def post():
        try:
            client.process_message(request.get_json())
        except Exception as e:
            logging.debug(e)

        return 'ok'


    @client.register_webhook(webhook_types.MESSAGE_RECEIVED)
    def message_received(webhook):
        logging.debug((webhook_types.MESSAGE_RECEIVED, webhook))


    @client.register_webhook(webhook_types.POSTBACK_RECEIVED)
    def postback_received(webhook):
        logging.debug((webhook_types.POSTBACK_RECEIVED, webhook))


    @client.register_webhook(webhook_types.AUTHENTICATION)
    def authentication(webhook):
        logging.debug((webhook_types.AUTHENTICATION, webhook))


    @client.register_webhook(webhook_types.ACCOUNT_LINKING)
    def account_linking(webhook):
        logging.debug((webhook_types.ACCOUNT_LINKING, webhook))


    @client.register_webhook(webhook_types.MESSAGE_DELIVERED)
    def message_delivered(webhook):
        logging.debug((webhook_types.MESSAGE_DELIVERED, webhook))


    @client.register_webhook(webhook_types.MESSAGE_READ)
    def message_read(webhook):
        logging.debug((webhook_types.MESSAGE_READ, webhook))


    @client.register_webhook(webhook_types.MESSAGE_ECHO)
    def message_echo(webhook):
        logging.debug((webhook_types.MESSAGE_ECHO, webhook))

