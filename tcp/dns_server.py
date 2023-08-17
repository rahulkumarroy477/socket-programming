import socket
import json
from random import choice
f = open("C:/Users/91707/Desktop/pynb/socket/tcp/dns.json","r")

data = json.load(f)

def search_json(key):    
    if key in data:
        print(key+ " is present")
    else:
        print(key + " is absent in dns.json")
        print("Plz wait adding it to file")
        l =[]
        for x in data.values():
            l.append(int(x))
        
        val = str(choice([i for i in range(11111,99999) if i not in l]))
        data[key]=val
        f.close()
        fp = open("C:/Users/91707/Desktop/pynb/socket/tcp/dns.json","w")
        json.dump(data,fp)
        fp.close()
    return data[key]


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
    
    key = conn.recv(1024).decode()

    send_data = search_json(key)
    print(send_data)
    conn.send(send_data.encode())

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()