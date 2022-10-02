from email import header
import socket
import datetime


class Server:
    def __init__(self) -> None:
        self.HEADERS = {'200':'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode('utf-8'),
                        '404':'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode('utf-8'), }
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('192.168.1.71', 80))
        self.server.listen()
        self.accept_client()

    def accept_client(self):
        while True:
            client, address = self.server.accept()
            path = client.recv(1024).decode('utf-8').split(' ')
            headers = client.recv(1024).decode('utf-8')
            print(headers)
            print(f'[{datetime.datetime.now()}] Request type "{path[0]}" {path[1]} from {address[0]}')
            client.send(self.Get(path[1]))
            client.shutdown(socket.SHUT_WR)

    def Get(self, path):
        path = path[1:]
        try:
            with open(path, 'rb') as file:
                data = file.read()
                file.close()
            return self.HEADERS['200'] + data

        except FileNotFoundError:
            return self.HEADERS['404'] + b'page is not found'


            

        
if __name__ == '__main__':
    Server()