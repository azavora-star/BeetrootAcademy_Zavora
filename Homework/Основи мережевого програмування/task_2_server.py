# Extend the echo server, which returns to client the data, encrypted using the Caesar cipher algorithm 
# by a specific key obtained from the client.

import socket

def ceasar_encryption(text,shift):
    global encryption 
    encryption = ""
    for c in text:
        if c.isalpha():
        # find the position in 0-25
            c_unicode = ord(c)
            c_index = ord(c) - ord("a")
        # perform the shift
            new_index = (c_index + shift) % 26
        # convert to new character
            new_unicode = new_index + ord("a")
            new_character = chr(new_unicode)
        # append to encrypted string
            encryption = encryption + new_character
        else:
            encryption = encryption + c   
    return encryption
    # print("Plain text:",text)
    # print("Encrypted text:",encryption)


HOST = '127.0.0.1'  # Standard loop-back interface address (localhost)
PORT = 7575        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    conn, addr = server_socket.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = (conn.recv(1024).decode()).strip()
            text = data[:-1]
            shift = int(data[-1:])
            ceasar_encryption(text,shift)
            if not data:
                break
            conn.sendall(encryption.encode())