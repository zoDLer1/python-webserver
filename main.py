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
            return self.response(file.read(), headers=[ContentType('Content-Type', types.get_type(extension), config.DEFAULT_CHARSET)])

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
      
    

    #    with open(path, mode) as file:    
    #         extention = path[:path.rfind('.')]
    #         return self.response(file.read(), {'Content-Type': types.get_type(extention)})


class Server:
    
    
    
    URLS = {
        'main': urls,
        'static': static_url,
    }
    
    DEFAULT_CHARSET = config.DEFAULT_CHARSET
    
    RESPONSE_HEADERS = {
        'protocol': 'HTTP/1.1',
        'content-type': 'text/html'
    }
    
    DEFAULT_PARSE_RULES = [
        lambda value: value.lower().strip()   
    ]
    
    HEADERS_PARSE_RULES = {
        'accept-encoding': lambda value: tuple(value.split(',')),
    }
    
    
    def __init__(self) -> None:
        self.HEADERS = {'200':'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode('utf-8'),
                        '404':'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode('utf-8'), }
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('localhost', 80))
        self.server.listen()
        self.accept_client()



    @classmethod
    def parse_headers(cls, str_info:str, user:tuple[socket.socket, tuple[str, int]]) -> Request:
        request_info, *headers_set = str_info.split('\r\n')
        headers = {}
        for header_info in headers_set:
            if header_info:
                header_name = Headers.name(header_info).lower()
                headers[header_name] = Headers.header(header_name).parse(header_info)
                
        user, address = user
        return Request(*request_info.split(' '), headers=headers, user=user, address=address)
        
    def accept_client(self):
        while True:
            user = client, address = self.server.accept()
            info = client.recv(1024).decode('utf-8')
            request =  self.parse_headers(info, user)
            print(f'[{datetime.datetime.now()}] Request type "{request.method}" {request.path} from {request.address[0]}')
            self.find_url(request)
            client.shutdown(socket.SHUT_WR)


    def find_url(self, request):
        for url in self.URLS:
            view_obj = self.URLS[url].path(request.path)
            if view_obj:
                break
        print(view_obj)
        if not view_obj:
            view_obj = Response_404
        
        response = getattr(view_obj(), request.method.lower())(request)
        response.send()
        # request.user.send('HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode('utf-8') + response.info.encode('utf-8'))




            

        
if __name__ == '__main__':
    Server()