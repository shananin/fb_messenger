from __future__ import unicode_literals

from fb_messenger import webhook_attachments
from fb_messenger.types import webhook_attachment_types


def test_parse_image():
    url = 'IMAGE_URL'
    payload = {
        'type': 'image',
        'payload': {
            'url': url,
        }
    }
    image = webhook_attachments.parse_payload(payload)

    assert isinstance(image, webhook_attachments.Image)
    assert image.url == url
    assert image.type == webhook_attachment_types.IMAGE


def test_parse_audio():
    url = 'AUDIO_URL'
    payload = {
        'type': 'audio',
        'payload': {
            'url': url,
        }
    }
    audio = webhook_attachments.parse_payload(payload)

    assert isinstance(audio, webhook_attachments.Audio)
    assert audio.url == url
    assert audio.type == webhook_attachment_types.AUDIO


def test_parse_video():
    url = 'VIDEO_URL'
    payload = {
        'type': 'video',
        'payload': {
            'url': url,
        }
    }
    video = webhook_attachments.parse_payload(payload)

    assert isinstance(video, webhook_attachments.Video)
    assert video.url == url
    assert video.type == webhook_attachment_types.VIDEO


def test_parse_file():
    url = 'FILE_URL'
    payload = {
        'type': 'file',
        'payload': {
            'url': url,
        }
    }
    file = webhook_attachments.parse_payload(payload)

    assert isinstance(file, webhook_attachments.File)
    assert file.url == url
    assert file.type == webhook_attachment_types.FILE


def test_parse_location():
    lat = 12.2323
    long = 12.2343
    payload = {
        'type': 'location',
        'coordinates': {
            'lat': 12.2323,
            'long': 12.2343,
        }
    }
    location = webhook_attachments.parse_payload(payload)

    assert isinstance(location, webhook_attachments.Location)
    assert location.lat == lat
    assert location.long == long
    assert location.type == webhook_attachment_types.LOCATION
