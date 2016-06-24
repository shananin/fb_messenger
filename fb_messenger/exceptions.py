class FBMainException(Exception):
    pass


class IncorrectFBRequest(FBMainException):
    pass


class UnknownCallback(FBMainException):
    pass


class FBRequestFailed(FBMainException):
    pass


class FBIncorrectType(FBMainException):
    pass


class FBIncorrectResponse(FBMainException):
    pass
