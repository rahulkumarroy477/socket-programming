
import socket
def cal(n1,n2,op):
    if op == "+":
        return str(n1+n2)
    elif op == "-":
        return str(n1-n2)
    elif op == "*":
        return str(n1*n2)
    else:
        if n2==0:
            return "error"
        else:
            return str(n1/n2)

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 4455

    """ Creating the UDP socket """
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    """ Bind the host address with the port """
    server.bind((host, port))
    while True:
        data, addr = server.recvfrom(1024)
        data = data.decode("utf-8")
        if data == "exit":
            print("Client disconnected.")
            break
        val = data.split()
        print(f"num1 = {val[0]}\nnum2 = {val[1]}\noperation = {val[2]}")
        data = cal(int(val[0]),int(val[1]),val[2])
        print(data)
        data = data.encode("utf-8")
        server.sendto(data, addr)
        
    server.close()