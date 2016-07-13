from __future__ import unicode_literals
from fb_messenger.client import FBMessenger
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
test = load_dotenv(dotenv_path)

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

