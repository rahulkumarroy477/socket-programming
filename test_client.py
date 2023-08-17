import socket

host = socket.gethostname()  # as both code is running on same pc
port = 5000  

client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))
filename = client_socket.recv(1024).decode()
filename = "_"+filename
with open(filename, "wb") as f:
    while True:
        bytes_read = client_socket.recv(1024)
        if not bytes_read:
            break
        f.write(bytes_read)

f.close()
client_socket.close()



