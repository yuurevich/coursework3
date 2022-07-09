
class BaseServiceError(Exception):
    code = 500


class ItemNotFound(BaseServiceError):
    code = 404


class WrongPasswords(BaseServiceError):
    pass


class UserAlreadyExists(BaseServiceError):
    pass


class UserNotFound(BaseServiceError):
    pass