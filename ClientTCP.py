import socket

target_host = 'localhost'
target_port = 8000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host,target_port))
client.sendall(str.encode('Bom dia Carai!'))
data = client.recv(1024)

print ('Mensagem ecoada:', data.decode())