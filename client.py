import socket

host = '127.0.0.1'
port = 54322

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to the server.")
except ConnectionRefusedError:
    print("Connection failed. Is the server running?")
    exit()

try:
    message = input("Enter your message (type 'over' to exit): ")

    while message.lower().strip() != "over":
        client_socket.send(message.encode())
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                print("Server disconnected.")
                break
            print("Server says:", data)
        except Exception as e:
            print("Error receiving data:", str(e))
            break

        message = input("Enter your message (type 'over' to exit): ")
finally:
    client_socket.close()
    print("Disconnected!")
