import socket

target_host = 'localhost'
target_port = 50000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
while True:
    msg = input('Digite Sua msg:') 
    client.sendall(str.encode(msg))
    data = client.recv(1024)

    print ('Mensagem ecoada:', data.decode())