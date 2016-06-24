class FBMessengerException(Exception):
    pass


class IncorrectFBRequest(FBMessengerException):
    pass


class UnknownCallback(FBMessengerException):
    pass


class FBRequestFailed(FBMessengerException):
    pass
