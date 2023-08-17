import socket
 # get the hostname
host = socket.gethostname()
port = 5000  # initiate port no above 1024

server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
server_socket.bind((host, port))  # bind host address and port together

server_socket.listen(2)
conn, address = server_socket.accept()  # accept new connection
print("Connection from: " + str(address))

data = conn.recv(1024).decode()
op = str(data)
data = conn.recv(1024).decode()
num1 = int(str(data))
data = conn.recv(1024).decode()
num2 = int(str(data))


if op=="+":
    ans = str(num1+num2)
elif op =="-":
    ans = str(num1-num2)
elif op == "*":
    ans = str(num1*num2)
else:
    ans = str(num1/num2)
conn.send(ans.encode())


conn.close()