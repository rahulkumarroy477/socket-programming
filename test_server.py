import socket
host = socket.gethostname()
port = 5000  

server_socket = socket.socket()  
server_socket.bind((host, port))  

server_socket.listen(2)
conn, address = server_socket.accept() 
filename = input("Enter file name to send : ")
conn.sendall(filename.encode())
with open(filename, "rb") as f:
    while True:
        bytes_read = f.read(1024)
        if not bytes_read:
            break
        conn.sendall(bytes_read)
f.close()
print("File sent successfully")

conn.close()