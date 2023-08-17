import socket

def checkReceiverChecksum(ReceivedMessage,k,Checksum):
    # Dividing sent message in packets of k bits.
    c1 = ReceivedMessage[0:k]
    c2 = ReceivedMessage[k:2*k]
    c3 = ReceivedMessage[2*k:3*k]
    c4 = ReceivedMessage[3*k:4*k]
 
    # Calculating the binary sum of packets + checksum
    ReceiverSum = bin(int(c1, 2)+int(c2, 2)+int(Checksum, 2) +
                      int(c3, 2)+int(c4, 2)+int(Checksum, 2))[2:]
 
    # Adding the overflow bits
    if(len(ReceiverSum) > k):
        x = len(ReceiverSum)-k
        ReceiverSum = bin(int(ReceiverSum[0:x], 2)+int(ReceiverSum[x:], 2))[2:]
 
    # Calculating the complement of sum
    ReceiverChecksum = ''
    for i in ReceiverSum:
        if(i == '1'):
            ReceiverChecksum += '0'
        else:
            ReceiverChecksum += '1'
    return ReceiverChecksum

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
    
    data = conn.recv(1024).decode()
    print(data)
    c_checksum = conn.recv(1024).decode()
    print(c_checksum)
    r_checksum = checkReceiverChecksum(data,8,c_checksum)


    finalsum=bin(int(c_checksum,2)+int(r_checksum,2))[2:]

    finalcomp=''
    for i in finalsum:
        if(i == '1'):
            finalcomp += '0'
        else:
            finalcomp += '1'

    # If sum = 0, No error is detected
    if(int(finalcomp,2) == 0):
        data = "Correct data"
        
    # Otherwise, Error is detected
    else:
        data = "Incorrect"

    conn.send(data.encode()) 

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()