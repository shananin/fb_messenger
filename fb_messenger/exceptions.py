"""
Exception collection
"""
# pylint: disable=super-init-not-called
class MainException(Exception):
    pass


class UnknownCallback(MainException):
    pass


class RequestFailed(MainException):
    pass


class IncorrectType(MainException):
    pass


class IncorrectResponse(MainException):
    pass


class UnknownAction(MainException):
    pass


class UnknownNotificationType(MainException):
    pass


class InvalidBody(MainException):
    pass


class MessengerAPIError(MainException):
    def __init__(self, response_dict):
        if 'error' not in response_dict:
            return

        self.message = response_dict['error'].get('message', '')
        self.type = response_dict['error'].get('type', '')
        self.code = response_dict['error'].get('code', '')
        self.fbtrace_id = response_dict['error'].get('fbtrace_id', '')

    def __str__(self):
        return self.message

    def __unicode__(self):
        return self.__str__()
