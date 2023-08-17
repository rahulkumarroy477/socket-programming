import socket

def crc_generator(data, generator):
   
    # Generate the CRC code for the given data and generator.
    data = [int(x) for x in data]
    generator = [int(x) for x in generator]
    n = len(data)
    m = len(generator)
    data = data + [0] * (m - 1)
    for i in range(n):
        if data[i] == 1:
            for j in range(m):
                data[i + j] = data[i + j] ^ generator[j]
    crc = data[-m+1:]
    return ''.join(str(x) for x in crc)


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    data = input("Enter data: > ")  # take input
    generator = input("Enter generator: >")
    data = data+crc_generator(data,generator)
    print(data)
    client_socket.send(data.encode())
    client_socket.send(generator.encode())
    data = client_socket.recv(1024).decode()
    print('Received from server: ' + data)


if __name__ == '__main__':
    client_program()