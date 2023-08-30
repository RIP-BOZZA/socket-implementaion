from socket import *

serverport=12000
server_socket=socket(AF_INET,SOCK_DGRAM)
server_socket.bind(('',serverport))
print('server is ready')
while 1:
    msg,client_address=server_socket.recvfrom(2048)
    modified_message=msg.upper()
    print(msg,client_address)
    server_socket.sendto(modified_message,client_address)
