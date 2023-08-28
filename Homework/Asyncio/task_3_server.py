# Echo server with asyncio
# Create a socket echo server which handles each connection using asyncio Tasks.

import socket
import asyncio

HOST = '127.0.0.1'
PORT = 7575

async def client_handling(conn, addr):
    while True:
        data = await conn.recv(1024)
        if not data:
            break
        await conn.sendall(data.upper())

async def main():
    loop = asyncio.get_event_loop()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    
    while True:
        conn, addr = await loop.sock_accept(server)
        print('Connected by', addr)
        asyncio.create_task(client_handling(conn, addr))

asyncio.run(main())