from ..exceptions.http_exceptions import HttpException
from .request import Request
from settings import SERVER, DEFAULT_CHARSET
from .headers import HeadersSet
from datetime import datetime
from ..readers.files import FileReader

class Response:

    def __init__(self, request: Request, body: bytes = b'', status=200, headers=[], cookies=[]) -> None:
        self.request = request
        self.headers = self.server_headers()
        self.body = body
        self.status = status

    @property
    def encoded_headers(self):
        if ((not self.headers['Content-Type']) and self.body):
            self.headers['Content-Type'] = 'text\plain'
        encoded = (f'{self.request.protocol} {self.status}\r\n' + self.headers.prepare() + '\r\n').encode(DEFAULT_CHARSET)
        return encoded

    def server_headers(self):
        return HeadersSet({
            'Server': SERVER,
            'Date': datetime.ctime(datetime.now())
        })

    def prepare(self):
        if (self.body):
            self.headers['Content-Length'] = len(self.body)
        return self.encoded_headers + self.body

    @classmethod
    def from_exception(cls, request, exception: HttpException):
        return cls(request, status=exception.status)

class RedirectResponse(Response):
    def __init__(self, request: Request, redirect_url, headers=[], cookies=[]) -> None:
        super().__init__(request, status=301, headers=headers, cookies=cookies)
        self.headers['Location'] = redirect_url

class FileResponse(Response):

    def __init__(self, request, filepath, status=200, headers=[], cookies=[]) -> None:
        super().__init__(request, status=status, headers=headers, cookies=cookies)
        reader = FileReader(filepath)
        if (reader.mimetype):
            self.headers['Content-Type'] = reader.mimetype
        self.body = reader.content


