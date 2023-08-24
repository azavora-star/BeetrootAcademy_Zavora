import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 7575        # The port used by the server

txt_to_encrypt = "python is the best"
cipher_shift = 2
data = txt_to_encrypt + str(cipher_shift)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    client_socket.sendall(data.encode())
    data = client_socket.recv(1024)

print('Received', repr(data))