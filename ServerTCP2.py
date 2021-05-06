import socket
import threading

bind_ip = 'localhost'
bind_port = 50000

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)

print ('aguardando conexão')
conn, ender = server.accept()

print('Conectado em', ender)

while True:
    client = conn.recv(1024)
    if not client:      
        conn.close()        
        break
    
    if client.decode() == "-close":
        conn.close()
        print("cliente fechou conexão!!!")
        break
    print (client.decode())
        
    msg = input('Digite Sua msg:')    
    conn.sendall(str.encode(msg))   
    
    
    if msg == "-close":        
        conn.close()
        break
    