import config
import socket
import datetime
from dataclasses import dataclass
from urls import urls, static_url
from handler import Response_404
from MIME_types import types
from headers import Headers, ContentType





@dataclass
class Request:
    method: str
    path: str
    protocol: str
    headers: dict
    user: socket.socket
    address: tuple[str, int]

    def render(self, path, mode='r'):
        with open(path, mode) as file:
            extension = path[path.rfind('.')+1:]
            return self.response(file.read(), headers=[ContentType(types.get_type(extension), config.DEFAULT_CHARSET)])

    def response(self, info, headers={}, status_code=200):
        hdrs = f" {self.protocol} {status_code}\r\n"
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
            self.info = self.info.encode(Server.DEFAULT_CHARSET)
        
        self.request.user.send(self.str_headers.encode(Server.DEFAULT_CHARSET) + self.info)
      
    



class Server:
    
    URLS = {
        'main': urls,
        'static': static_url,
    }
    
    DEFAULT_CHARSET = config.DEFAULT_CHARSET
    
    def __init__(self) -> None:
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(config.HOST)
        self.server.listen()
        self.accept_client()

    @classmethod
    def parse_headers(cls, str_info:str, user:tuple[socket.socket, tuple[str, int]]) -> Request:
        request_info, *headers_set = str_info.split('\r\n')
        headers = [Headers.header(header_info) for header_info in headers_set if header_info]                
        user, address = user
        return Request(*request_info.split(' '), headers=headers, user=user, address=address)
        
    def accept_client(self):
        while True:
            user = client, address = self.server.accept()
            info = client.recv(1024).decode('utf-8')
            # info2 = client.recv(2048).decode('utf-8')
            # print('1', info)
            # print('----------')
            # print('2', info2)
            request =  self.parse_headers(info, user)
            print(f'[{datetime.datetime.now()}] Request type "{request.method}" {request.path} from {request.address[0]}')
            self.find_url(request)
            client.shutdown(socket.SHUT_WR)

    def find_url(self, request):
        for url in self.URLS:
            view_obj = self.URLS[url].path(request.path)
            if view_obj:
                break
        if not view_obj:
            view_obj = Response_404
        
        response = getattr(view_obj(), request.method.lower())(request)
        response.send()





            

        
if __name__ == '__main__':
    Server()