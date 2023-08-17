import socket

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)     # object of socket
s.bind((socket.gethostname(),1234))
s.listen(5)

while True:
    clientsocket,address = s.accept()
    print(f"connection from {address} is established")
    clientsocket.send(bytes("Hello there, welcome to server!","utf-8"))
    
    clientsocket.close()
