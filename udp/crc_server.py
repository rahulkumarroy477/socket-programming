import socket


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 4455
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))
    while True:
        data, addr = server.recvfrom(1024)
        data = data.decode("utf-8")
        if data == "exit":
            print("Client disconnected.")
            break
        key,addr = server.recvfrom(1024)
        key = key.decode("utf-8")
        print(data)
        print(key)
        

        
        data = data.encode("utf-8")
        server.sendto(data, addr)
        
    server.close()