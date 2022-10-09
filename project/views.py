from turtle import pen
from requests import delete
from core.views_objects.view import View
from core.requests_objects.headers import Access_Control_Allow_Methods, Access_Control_Allow_Origin, Access_Control_Allow_Headers


  

    
class MyView(View):
    def get(self, request):        
        return request.render('index.html')
    
    def post(self, request):
        return super().post(request)
    
class TestView(View):
    def post(self, request):
        return request.response(info='OKEY', headers=[Access_Control_Allow_Origin('*'), 
                                                        Access_Control_Allow_Methods('*'),
                                                        Access_Control_Allow_Headers('*')])
    def delete(self, request):
        print(request.data['firstName'])
        return super().delete(request)
        