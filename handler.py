import config

class View:
    def request(self, request):
        return request.response(f'"{request.method}" {request.path}  from {request.address[0]}')
        
    def get(self, request):
        return self.request(request)
    
    def post(self, requst):
        return self.request(requst)
    

class FileReader:
    def get(self, request):
        # for i in request.headers:
        #     print(request.headers[i])
        # print(request.headers)
        return request.render(config.STATIC_FOLDER + request.path, mode='rb')
        
    
class Response_404(View):
    def request(self, request):
        return request.response(f'', status_code=404)