import socket
import datetime
from dataclasses import dataclass
from urls import urls


@dataclass
class Request:
    method: str
    path: str
    protocol: str
    headers: dict
    user: socket.socket
    address: tuple[str, int]

    def response(self, headers={}, status_code=200):
        pass
    
    
class Response:
    code: int 
    request: Request
    info: str
    headers: dict


        


class Server:
    
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
    def normalize_header(cls, header:str):
        key, value = header.split(': ')
        for rule in cls.DEFAULT_PARSE_RULES:
            key = rule(key)
            value = rule(value)
        if key in cls.HEADERS_PARSE_RULES:
            value = cls.HEADERS_PARSE_RULES[key](value)
        return key, value

    @classmethod
    def parse_headers(cls, str_info:str, user:tuple[socket.socket, tuple[str, int]]) -> Request:
        request_info, *headers_set = str_info.split('\r\n')
        headers = {}
        for header in headers_set:
            if header:
                print(header)
                key, value = cls.normalize_header(header)
                headers[key] = value
        user, address = user
        
        return Request(*request_info.split(' '), headers=headers, user=user, address=address)
        
       
        
        
    def accept_client(self):
        while True:
            user = client, address = self.server.accept()
            info = client.recv(1024).decode('utf-8')
            request =  self.parse_headers(info, user)
            print(f'[{datetime.datetime.now()}] Request type "{request.method}" {request.path} from {request.address[0]}')
            self.find_url(request)
            # client.send(self.Get(request.path))
            # client.shutdown(socket.SHUT_WR)

    def find_url(self, request):
        view_obj = urls.path(request.path)()
        response_info = getattr(view_obj, request.method.lower())(request)
        
        request.user.send('HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode('utf-8') + response_info.encode('utf-8'))


    # def Get(self, path):
    #     path = path[1:]
    #     try:
    #         with open(path, 'rb') as file:
    #             data = file.read()
    #             file.close()
    #         return str(self.HEADERS['200']).encode('utf-8')

    #     except FileNotFoundError:
    #         return self.HEADERS['404'] + b'page is not found'


            

        
if __name__ == '__main__':
    Server()