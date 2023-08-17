import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpHost = '127.0.0.1'
udpPort = 12345
msg = input('Enter the message to send: ')
mess = ''.join(format(ord(i), '08b') for i in msg)
packetSize = 8 #8bit packet size!
packets = []

if(len(mess) > packetSize):
    i = 0
    j = 8
    while(j<= len(mess)):
        packets.append(mess[i:j])
        i = j
        j = j+8

index = 0
while(index<len(packets)):
    flag = 0
    while(flag == 0):
        sock.sendto(packets[index].encode(),(udpHost,udpPort))
        ackn = sock.recv(1024)
        if(int(ackn.decode()) == 1):
            print(f"Packet {index} sent successfully")
            index+=1
            flag = 1
        else:
            print(f"Packet {index} sent unsuccessfully, resending..")

sock.sendto("END".encode(),(udpHost,udpPort))











    

