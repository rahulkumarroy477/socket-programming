import socket


def server_program():


    fac = [1,1]
    for i in range(2,1000):
        fac.append(fac[i-1]*i)


    # get the hostname
    host = socket.gethostname()
    port = 5000  

    server_socket = socket.socket()  
   
    server_socket.bind((host, port))  # bind host address and port together

    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    data = conn.recv(1024).decode()
    print("Number received from user : " + str(data))
    data = str(fac[int(str(data))])
    conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()