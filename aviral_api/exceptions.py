class BaseException(Exception):
    def __init__(self, message) -> None:
        self.message = message

class WrongLoginError(BaseException):
    pass

class AviralDownError(BaseException):
    pass

class InvalidResponseError(BaseException):
    pass

class InvalidSessionError(BaseException):
    pass

class UserNotLoggedInError(BaseException):
    pass