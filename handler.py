class View:
    
    def request(self, request):
        return f'"{request.method}" {request.path}  from {request.address[0]}'
        
    def get(self, request):
        return self.request(request)
    
    def post(self, requst):
        return self.request(requst)