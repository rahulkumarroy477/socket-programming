import socket

def check_crc(data, generator):
    
    # Check if the given data and generator produce the given crc code.
    
    data = [int(x) for x in data]
    generator = [int(x) for x in generator]
    n = len(data)
    m = len(generator)
    for i in range(n - m + 1):
        if data[i] == 1:
            for j in range(m):
                data[i + j] = data[i + j] ^ generator[j]
    remainder = data[-m+1:]
    return all(r == 0 for r in remainder)
def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    
    data = conn.recv(1024).decode()
    print(data)
    generator = conn.recv(1024).decode()
    print(generator)
    print("User--> " + str(data))
    data = check_crc(data,generator)
    print(data)
    if data:
        data = "Server--> Received Correct data"
    else:
        data = "Server--> Received corrupted data"
    conn.send(data.encode())  

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()