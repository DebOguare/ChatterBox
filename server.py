import socket

host = '127.0.0.1'
port = 54322

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()

print("Server is waiting for connections...")

conn, addr = server_socket.accept()
print("Client connected from:", addr)

print("Type 'quit' to end the chat.")

while True:
    data = conn.recv(1024).decode()
    if not data or data.lower().strip() == 'over':
        print("Client disconnected.")
        break
    print("Client says:", data)
    
    response = input("You (Server): ")
    conn.send(response.encode())
    if response.lower().strip() == 'over':
        print("You ended the chat.")
        break

conn.close()
server_socket.close()
print("Server stopped.")

