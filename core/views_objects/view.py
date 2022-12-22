from core.requests_objects.headers import Access_Control_Allow_Methods, Access_Control_Allow_Origin, Access_Control_Allow_Headers
import config

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
        
    def delete(self, request):
        return self.request(request)
    
    def put(self, request):
        return self.request(request)
    
class FileReader:
    def get(self, request):
        return request.render(config.STATIC_FOLDER + request.path, mode='rb')
    
class Response_404(View):
    def request(self, request):
        return request.response(f'', status_code=404)