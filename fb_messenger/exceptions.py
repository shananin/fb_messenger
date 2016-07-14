class MainException(Exception):
    pass


class IncorrectRequest(MainException):
    pass


class UnknownCallback(MainException):
    pass


class RequestFailed(MainException):
    pass


class IncorrectType(MainException):
    pass


class IncorrectResponse(MainException):
    pass
