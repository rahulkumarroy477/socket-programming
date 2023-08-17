
import socket


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 4455

    """ Creating the UDP socket """
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    """ Bind the host address with the port """
    server.bind((host, port))
    fact = [1,1]
    for i in range(2,500):
        fact.append(fact[i-1]*i)
    while True:
        data, addr = server.recvfrom(1024)
        data = data.decode("utf-8")
        if data == "!EXIT":
            print("Client disconnected.")
            break
        print(f"Client> {data}")
        val = int(data)
        data = str(fact[val])
        data = data.encode("utf-8")
        server.sendto(data, addr)
        
    server.close()