from src.data_handlers.response import Request, FileResponse
from src.controller import Controller

class MainController(Controller):

    def index(self, request: Request):
        return FileResponse(request, 'pages/album.html')

