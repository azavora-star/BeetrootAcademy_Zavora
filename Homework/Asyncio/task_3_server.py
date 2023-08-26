# Echo server with asyncio
# Create a socket echo server which handles each connection using asyncio Tasks.


import socket
import asyncio

HOST = '127.0.0.1'  # Standard loop-back interface address (localhost)
PORT = 7575        # Port to listen on (non-privileged ports are > 1023)

async def client_handling(addr, conn):
     while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data.upper())

async def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
    
    task1 = asyncio.create_task(client_handling(addr, conn))
    await asyncio.gather(task1)

asyncio.run(main())            

            