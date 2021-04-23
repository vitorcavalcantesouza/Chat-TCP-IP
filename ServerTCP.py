import socket
import threading

bind_ip = 'localhost'
bind_port = '8000'

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)
