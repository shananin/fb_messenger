import codecs
import os
import re

from setuptools import setup


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *parts), 'r', 'utf-8') as f:
        return f.read()


# def find_version(*file_paths):
#     """
#     Build a path from *file_paths* and search for a ``__version__``
#     string inside.
#     """
#     version_file = read(*file_paths)
#     version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
#                               version_file, re.M)
#     if version_match:
#         return version_match.group(1)
#     raise RuntimeError("Unable to find version string.")


if __name__ == "__main__":
    setup(

        classifiers=[
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: Implementation :: CPython',
            'Programming Language :: Python :: Implementation :: PyPy',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],
        description="Python API client for FB Messenger",
        long_description=read('README.rst'),
        install_requires=[
        ],
        keywords="fb facebook messenger client api chat",
        license="MIT",
        name="fb_messenger",
        packages=["fb_messenger", "fb_messenger.types"],
        url="https://github.com/shananin/Fb_messanger",
        version='0.1.1',
        maintainer='Artem Shananin (Shananin)',
        maintainer_email='artem.shananin@gmail.com',
    )
