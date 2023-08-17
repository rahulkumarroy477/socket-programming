import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    data = input("Enter key : ")
    print(data)
    client_socket.send(data.encode())
    data = client_socket.recv(1024).decode()
    print('Received from server: ' + data)


if __name__ == '__main__':
    client_program()