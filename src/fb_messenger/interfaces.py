class IFBPayload(object):
    def get_dict(self):
        raise NotImplementedError('Should have implemented get_dict method')


class IButton(IFBPayload):
    pass
