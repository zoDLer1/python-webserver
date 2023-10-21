class HttpException(Exception):
    status = 500

class UnsupportedMediaType(HttpException):
    status = 415

class NotFound(HttpException):
    status = 404
