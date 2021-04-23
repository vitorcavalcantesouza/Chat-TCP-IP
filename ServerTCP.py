import socket
import threading

bind_ip = 'localhost'
bind_port = 8000

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen()
print ('aguardando conexão')
conn, ender = server.accept()

print('Conectado em', ender)


while True:
    data = conn.recv(1024)
    if not data:
        print('Fechando a conexão')
        conn.close()
        break
    conn.sendall(data)