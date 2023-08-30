from socket import *

server_name='localhost'
server_port=12000
client_socket=socket(AF_INET,SOCK_DGRAM)
message=input('first message')
message_enc=bytes(message,'utf-8')
client_socket.sendto(message_enc,(server_name,server_port))# here the client port is not mentioned,we let the os do this
modified_message,server_address=client_socket.recvfrom(2048)
print(modified_message)
client_socket.close()