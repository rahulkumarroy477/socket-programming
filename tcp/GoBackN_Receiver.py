import time
import random
import socket

def BinaryToDecimal(binary):
    string = int(binary, 2)
    return string

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpHost = '127.0.0.1'
udpPort = 12345
sock.bind((udpHost,udpPort))
data = []
index = 0
while(True):
    msg,addr = sock.recvfrom(1024)
    if(msg.decode() != "END"):
        time.sleep(1)
        ackn = random.randint(0,1)
        if(ackn == 1):
            data.append(msg.decode())
            index+=1
        sock.sendto(str(ackn).encode(),addr)
    else:
        dataRecv = ''
        for item in data:
            dataRecv+= item
        str_data =''
        for i in range(0, len(dataRecv), 8):
            temp_data = dataRecv[i:i+8]
            decimal_data = BinaryToDecimal(temp_data)
            str_data = str_data + chr(decimal_data)
        print(str_data)
        break


