from src.data_handlers.response import Request, FileResponse
from src.controller import HttpController

class MainController(HttpController):

    def get(self, request: Request):
        return FileResponse(request, 'pages/album.html')

