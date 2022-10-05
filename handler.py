import config
from headers import Access_Control_Allow_Methods, Access_Control_Allow_Origin, Access_Control_Allow_Headers

class View:
    def request(self, request):
        return request.response(f'"{request.method}" {request.path}  from {request.address[0]}')
        
    def get(self, request):
        return self.request(request)
    
    def post(self, request):
        return self.request(request)
    
    
    def options(self, request):
        return request.response(headers=[Access_Control_Allow_Origin('*'), 
                                         Access_Control_Allow_Methods('*'),
                                         Access_Control_Allow_Headers('*')])
    
class FileReader:
    def get(self, request):
        return request.render(config.STATIC_FOLDER + request.path, mode='rb')
  
class Response_404(View):
    def request(self, request):
        return request.response(f'', status_code=404)
    
class MyView(View):
    def get(self, request):
        
        # print(request.headers)
        
        return request.render('index.html')
    def post(self, request):
        # for header in request.headers:
        #     print(request.headers[header])
        return super().post(request)
    
class TestView(View):
    def post(self, request):
        return request.response(info='OKEY', headers=[Access_Control_Allow_Origin('*'), 
                                         Access_Control_Allow_Methods('*'),
                                         Access_Control_Allow_Headers('*')])