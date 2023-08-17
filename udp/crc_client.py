import socket

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 4455
    addr = (host, port)

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        data = input("> String : ")
        key = input("   Key : ")

        # using join() + ord() + format()
        # Converting String to binary
        data = ''.join(format(ord(i), '08b') for i in data)
        # print(data)
        data = data.encode("utf-8")
        key = key.encode("utf-8")
        client.sendto(data, addr)
        client.sendto(key,addr)

        data, addr = client.recvfrom(1024)
        data = data.decode("utf-8")
        print(f"Server: {data}")
    
