from .routing import Router
from .data_handlers.response import Response, Request

class Application:

    def __init__(self, router: Router) -> None:
        self.router = router

    def run(self, request: Request) -> Response:
        return self.router.run(request)
