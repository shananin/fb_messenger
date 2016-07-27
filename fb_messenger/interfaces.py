"""
Interfaces collection
"""
from __future__ import unicode_literals


class IAttachment(object):
    def to_dict(self):
        raise NotImplementedError('Should have implemented to_dict method')


class ISubElement(object):
    def to_dict(self):
        raise NotImplementedError('Should have implemented to_dict method')
