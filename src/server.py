import socket
import settings
from src.debug import Debug
from src.data_handlers.request import Request
from src.data_handlers.response import Response
from src.exceptions.http_exceptions import HttpException
from .application import Application


class Server:

    def __init__(self, app: Application) -> None:
        self.app = app
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(settings.HOST)
        self.server.listen()
        self.accept_client()

    def send(self, client: socket.socket, response: Response):
        client.send(response.prepare())
        client.shutdown(socket.SHUT_WR)

    def run_application(self, data) -> Response:
        request = Request.parse(data)
        try:
            return self.app.run(request)
        except HttpException as exception:
            return Response.from_exception(request, exception)

    def accept_client(self):
        while True:
            user = self.server.accept()
            client, address = user
            data = client.recv(1024).decode('utf-8')
            response = self.run_application(data)
            self.send(client, response)
