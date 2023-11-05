class StatusCode:
    status = 0
    description = ''

    def __str__(self):
        return f'{self.status} {self.description}'


class Ok(StatusCode):
    status = 200
    description = 'Ok'


class NotFound(StatusCode):
    status = 404
    description = 'Not Found'

class UnsupportedMediaType(StatusCode):
    status = 415
    description = 'Unsupported Media Type'

class MethodNotAllowed(StatusCode):
    status = 405
    description = 'Method Not Allowed'
   

class InternalServerError(StatusCode):
    status = 500
    description = 'Internal Server Error'

class PermanentRedirect(StatusCode):
    status = 308
    description = 'Permanent Redirect'