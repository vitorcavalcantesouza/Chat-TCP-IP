import socket
import threading
import os

bind_ip = 'localhost'
bind_port = 50000

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)

print ('aguardando conexão')
conn, ender = server.accept()

print('Conectado em', ender)

while True:
    client = conn.recv(1024).decode()
    if not client:      
        conn.close()        
        break
    
    print (client)
        
    msg = input('Digite Sua msg:')    
    conn.sendall(str.encode(msg))   
    
    if msg == "-arquivo":
        namefile = str(input("arquivo> "))
        conn.send(namefile.encode())
        with open(namefile, 'rb') as file:
            for data in file.readlines():
                conn.send(data)
        
        print("arquivo enviado!!!")        
    
    if msg == "-close":        
        conn.close()
        break
    
