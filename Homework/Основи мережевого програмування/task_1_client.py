import socket

HOST = '127.0.0.1'  # Standard loop-back interface address (localhost)
PORT = 7575        # Port to listen on (non-privileged ports are > 1023)

# creating UDP client socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    client_socket.sendto(b"Hello, UDP-server", (HOST,PORT))
    data = client_socket.recvfrom(1024)
    print(f'This is msg from server -{data[0]}')
