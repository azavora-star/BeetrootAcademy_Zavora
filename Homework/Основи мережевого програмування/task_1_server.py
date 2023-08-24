# Task 1

# During the lesson, we have created a server and client, 
# which use TCP/IP protocol for communication via sockets. 
# In this task, you have to create a server and client, which will use user datagram protocol (UDP) for communication.

import socket

HOST = '127.0.0.1'  # Standard loop-back interface address (localhost)
PORT = 7575        # Port to listen on (non-privileged ports are > 1023)

# creating UDP server socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))

# listening incoming msgs    
    while True:
            data = server_socket.recvfrom(1024)
            message = data[0]
            address = data[1]
            print(f'this is the message {message} from this address {address}')

            # responding back to client
            server_socket.sendto(b'hello UDP-client', address)