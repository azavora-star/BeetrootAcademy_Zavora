# Echo server with threading
# Create a socket echo server that handles each connection using the multiprocessing library.

import socket
import multiprocessing

HOST = '127.0.0.1'  # Standard loop-back interface address (localhost)
PORT = 7575       # Port to listen on (non-privileged ports are > 1023)

def handle_client(addr):
    while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data.upper())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        client_process = multiprocessing.Process(target=handle_client, args=(addr,))
        client_process.start()