from dataclasses import dataclass
import config
import socket
from core.requests_objects.headers import ContentType, Headers
from core.requests_objects.MIME_types import types

@dataclass
class Request:
    method: str
    path: str
    protocol: str
    params : str
    headers: Headers
    user: socket.socket
    address: tuple[str, int]
    data = {}

    def render(self, path, mode='r'):
        path = config.PROJECT_FOLDER + '/' + path
        with open(path, mode) as file:
            extension = path[path.rfind('.')+1:]
            return self.response(file.read(), headers=[ContentType(types.get_type(extension), config.DEFAULT_CHARSET)])

    def response(self, info='', headers=[], status_code=200):
        hdrs = f"{self.protocol} {status_code}\r\n"
        for header in headers:
            hdrs += header.to_string()
        hdrs += '\r\n'
        
        
        return Response(self, info, hdrs, status_code)

@dataclass
class Response:
    request: Request
    info: str
    str_headers: str
    code: int 
    
    def send(self):
        if isinstance(self.info, str):
            self.info = self.info.encode(config.DEFAULT_CHARSET)
        
        self.request.user.send(self.str_headers.encode(config.DEFAULT_CHARSET) + self.info)