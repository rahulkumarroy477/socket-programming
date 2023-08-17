import socket

host = socket.gethostname()  # as both code is running on same pc
port = 5000  

client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server

message = input("Enter number : ")  # take input
client_socket.send(message.encode())
data = client_socket.recv(1024).decode()
data = int(data)
print(f"factorial of {message} = {data}")
client_socket.close()