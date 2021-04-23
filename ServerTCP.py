import socket
import threading

bind_ip = 'localhost'
bind_port = '8000'

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)
print '[*] Escutando %s:%d' %(bind_ip,bind_port)

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print '[*] recebido: %s' %request
    print '\n---------------------\n'
    client_socket.send('\nMensagem destinada ao cliente: %s\n' %addr[0])
    client_socket.send('\n ACK! \nRecebido pelo servidor!\n')
    client_socket.close()

while true:
    client, addr = server.accept()
    print '[*] Conexão aceita de:  %s:%d' %(addr[0], addr[1])
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()