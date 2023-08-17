import socket
import time
def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    # message = input(" -> ")  # take input

    # while message.lower().strip() != 'exit':
    while True:
        seconds = time.time()
        while True:

            data = client_socket.recv(1024).decode()  # receive response
            if seconds ==2:
                message = "False"
                client_socket.send(message.encode())  # send message
                break
            if data:
                if data=="exit":
                    break
                print('Received from server: ' + data)  # show in terminal
                message = "True"
                client_socket.send(message.encode())  # send message

                break
                


        # message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()