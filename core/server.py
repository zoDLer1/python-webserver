import socket
import config
import datetime
from core.views_objects.view import Response_404 
from core.requests_objects.headers import Headers
from core.requests_objects.objs import Request
from core.urls.static_url import StaticUrls
import json


class Server:
    
    URLS =  config.URLS + [StaticUrls()]
    DEFAULT_CHARSET = config.DEFAULT_CHARSET
    
    def __init__(self) -> None:
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(config.HOST)
        self.server.listen()
        self.accept_client()

    def parse_headers(self, str_info:str, user:tuple[socket.socket, tuple[str, int]]):
        request_info, *headers_set = str_info.split('\r\n')
        method, path, protocol = request_info.split(' ')
        path, params = self.parse_url(path)
        
        headers = Headers([Headers.header(header_info) for header_info in headers_set if header_info])               
        user, address = user
        return Request(method, path, protocol, params, headers, user, address)

    def parse_url(self, url: str):
        path, *params = url.split('?', 1)
        params = ''.join(params)
        dict_params = dict([param.split('=', 1) for param in params.split('&') if param]) 
        return path, dict_params
        
    def parse_data(self, data):
        return json.loads(data)
        
        
    def accept_client(self):
        
        while True:
            user = self.server.accept()
            client, address = user
            info = client.recv(1024).decode('utf-8')
            request = self.parse_headers(info, user)
            if request.headers.exists('content-length'):
                data = client.recv(int(request.headers.get('content-length').value)).decode('utf-8')
                request.data = self.parse_data(data)
                
                
            
            print(f'[{datetime.datetime.now()}] Request type "{request.method}" {request.path} from {request.address[0]}')
            self.find_url(request)
            client.shutdown(socket.SHUT_WR)
            
            # Thread(target=self.accept_request, args=[user]).start()
            # info2 = client.recv(2048).decode('utf-8')
            
            

    # def accept_request(self, user):
    #     client, address = user
    #     while True:
    #         info = client.recv(1024).decode('utf-8')
    #         # print('1', info)
    #         # print('----------')
    #         # print('2', info2)
    #         request = self.parse_headers(info, user)
    #         print(f'[{datetime.datetime.now()}] Request type "{request.method}" {request.path} from {request.address[0]}')
    #         self.find_url(request)
    #         client.shutdown(socket.SHUT_WR)


    def find_url(self, request):
        for url in self.URLS:
            view_obj = url.path(request.path)
            if view_obj:
                break
        if not view_obj:
            view_obj = config.DEFAULT_404_VIEW
        
        response = getattr(view_obj(), request.method.lower())(request)
        response.send()

