import socket
import time

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
    m=1
    while True:
        print("Message : "+str(m))
        data = input(' -> ')
        conn.send(data.encode())  

        # wait for acknowledgement
        seconds = time.time()
        while True:
            count = 1
            data = conn.recv(1024).decode()
            if seconds == 2:
                conn.send(data.encode())
                break
            if data == "True":
                print("\tAcknowledment "+str(count))
                break
            elif data == "False":
                conn.send(data.encode())
            elif data == "exit":
                break
        count+=1

    # conn.close()  # close the connection


if __name__ == '__main__':
    server_program()