import socket

host = socket.gethostname()  # as both code is running on same pc
port = 5000  

client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))
operation = input("Enter your operation : ")  # take input
client_socket.send(operation.encode())
num1 = input("Enter number 1 : ")
client_socket.send(num1.encode())
num2 = input("Enter number 2 : ")
client_socket.send(num2.encode())


data = client_socket.recv(1024).decode()
data = int(str(data))
print(f"{num1} {operation} {num2} = {data}")

client_socket.close()