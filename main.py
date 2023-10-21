from src.server import Server
from src.application import Application
from routes import router

if __name__ == '__main__':

    app = Application(router)
    Server(app)
