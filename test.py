import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.1.71', 80))
server.listen()

client, address = server.accept()
c = 0
client.send('HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode('utf-8') + b'')
while c < 10:
    client.send(f'{c}'.encode('utf-8'))
    time.sleep(2)