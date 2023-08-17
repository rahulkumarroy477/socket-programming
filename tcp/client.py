import socket

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))

# msg = s.recv(1024)      # 1024 is buffer size 
#  if we want to increase the size we should use loop
full_msg =''
while True:
    msg = s.recv(8)
    if len(msg)<=0:
        break;
    else:
        full_msg+=msg.decode("utf-8")
        # print(msg.decode("utf-8"))
print(full_msg)