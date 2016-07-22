"""
Interfaces collection
"""
from __future__ import unicode_literals


class IFBPayload(object):
    def to_dict(self):
        raise NotImplementedError('Should have implemented to_dict method')


class IButton(object):
    def to_dict(self):
        raise NotImplementedError('Should have implemented to_dict method')


class IGenericItem(object):
    def to_dict(self):
        raise NotImplementedError('Should have implemented to_dict method')
