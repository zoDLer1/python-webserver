from core.views_objects.view import View
from core.requests_objects.headers import Access_Control_Allow_Methods, Access_Control_Allow_Origin, Access_Control_Allow_Headers


  


    
class MyView(View):
    def get(self, request):        
        return request.render('index.html')
    
    def post(self, request):
        print(request.data)
        return super().post(request)
    
class TestView(View):
        
    def post(self, request):
        print(request.data)
        return request.response(info='OKEY', headers=[Access_Control_Allow_Origin('*')]) # + headers=[Access_Control_Allow_Origin('*'), Access_Control_Allow_Methods('*'), Access_Control_Allow_Headers('*')]
    
    def delete(self, request):
        return super().delete(request)
        