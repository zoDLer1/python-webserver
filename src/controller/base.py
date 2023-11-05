from ..exceptions.http_exceptions import MethodNotAllowedException

class Controller:
    def __init__(self, context) -> None:
        self.context = context

    @classmethod
    def as_view(cls, method):
        return ViewController(cls, method)

class ViewController:
    def __init__(self, controller_klass, method, context = {}) -> None:
        self.controller = controller_klass(context)
        self.method = getattr(self.controller, method)

    def __call__(self, *args, **kwds):
        return self.method(*args, **kwds)
    
class HttpController(Controller):
    
    def request(self, request):
        method = getattr(self, request.method.lower(), None)
        if not method:
            raise MethodNotAllowedException
        return method(request)

    @classmethod
    def as_view(cls):
        return ViewController(cls, 'request')