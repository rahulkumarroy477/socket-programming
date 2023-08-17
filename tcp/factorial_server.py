import socket

fac = [1,1]
for i in range(2,100):
    fac.append(fac[i-1]*i)
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
print("find factorial of : " + str(data))
index = int(str(data))
ans = fac[index]
conn.send(bytes(str(ans).encode()))
conn.close()

