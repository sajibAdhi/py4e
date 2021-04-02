import socket

mySocket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

mySocket.connect(('localhost', 80))
