# Echo server with threading
# Create a socket echo server which handles each connection in a separate Thread

import socket
import threading

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
        client_thread = threading.Thread(target=handle_client, args=(addr,))
        client_thread.start()