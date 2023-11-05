from ..status_codes.codes import NotFound, UnsupportedMediaType, MethodNotAllowed, InternalServerError


class HttpException(Exception):
    status_code = InternalServerError()

class UnsupportedMediaTypeException(HttpException):
    status_code = UnsupportedMediaType()

class NotFoundException(HttpException):
    status_code = NotFound()

class MethodNotAllowedException(HttpException):
    status_code = MethodNotAllowed()