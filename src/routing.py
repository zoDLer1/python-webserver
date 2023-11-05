from .data_handlers.request import Request
from .data_handlers.response import Response, FileResponse
from .helpers import normalize_url
from .exceptions.http_exceptions import NotFoundException
from .controller import ViewController
import os



class Route:

    def __init__(self, url: str, method: str, callback: tuple[ViewController, str]) -> None:
        self.url = normalize_url(url)
        self.method = method
        self.callback = callback

    def match(self, request: Request) -> bool:
        return self.url == normalize_url(request.url.path) and self.method == request.method

    def run(self, request: Request) -> Response:
        return self.callback(request)

class StaticFileRoute:

    def __init__(self, public_dir) -> None:
        self.public_dir = public_dir

    def run(self, request: Request) -> Response:
        return FileResponse(request, os.path.join(self.public_dir, request.url.path.strip('/')))

    def match(self, request: Request) -> bool:
        return os.path.isfile(os.path.join(self.public_dir, request.url.path.strip('/'))) and "GET" == request.method

class Router:
    routes: list[Route]

    def __init__(self) -> None:
        self.routes = []

    def register(self, url: str, method: str, callback):
        self.routes.append(Route(url, method, callback))

    def run(self, request: Request) -> Response:
        for route in self.routes:
            if route.match(request):
                return route.run(request)
        raise NotFoundException()

    def use_static(self, public_dir):
        self.routes.append(StaticFileRoute(public_dir))
