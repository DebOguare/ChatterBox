# TCP/IP Chat Application

## This project demonstrates an implementation of a bidirectional TCP/IP-based chat application in Python.

The project features a server-client communication system where:
- A server establishes a socket to listen for incoming client connections on a specified IP address and port.
- Upon successful connection, the server and client can send and receive messages interactively.
- The connection persists until either the server or client terminates communication by sending the predefined "over" command.

This project serves as a foundational implementation of the TCP/IP stack using Python's built-in `socket` library, demonstrating how to create and manage reliable message exchanges over a network.

## How to Set Up a Simple Server-Client Communication

1. **Install Python**
   - Download and install Python.

2. **Create a Project Directory**
   - Create a folder to house your project files.

3. **Set Up the Server and Client Scripts**
   - Create two Python files in the directory: `server.py` and `client.py`.
   - Copy and paste the respective server and client codes into these files.

4. **Run the Server**
   - Open a terminal and navigate to your project directory.
   - Run the server script:
     ```bash
     python server.py
     ```

5. **Run the Client**
   - Open another terminal in the same directory.
   - Run the client script:
     ```bash
     python client.py
     ```

6. **Start Chatting**
   - Type messages in the client terminal to send them to the server.
   - The server can respond interactively.

## Limitations
1. This implementation handles only one client connection at a time.
2. Both the server and client must run on the same machine using the loopback address (`127.0.0.1`).

## How It Works
- The server listens on a specified port for incoming client connections.
- Upon connection, both the server and client enter a communication loop.
- Messages are exchanged interactively until either side sends the "quit" command to terminate the session.

## Example Interaction
**Server Terminal:**
```
Server is waiting for connections...
Client connected from: ('127.0.0.1', 54321)
Type 'quit' to end the chat.
Client says: Hello, Server!
You (Server): Hi, Client!
Client says: How are you?
You (Server): I'm fine, thanks! You?
```

**Client Terminal:**
```
Connected to the server. Type 'quit' to end the chat.
You (Client): Hello, Server!
Server says: Hi, Client!
You (Client): How are you?
Server says: I'm fine, thanks! You?
```

## Resources
1. https://thepythoncode.com/article/make-a-chat-room-application-in-python
2. https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170
3. https://youtu.be/Ar94t2XhKzM?si=nfVn4bGkd_wMlL1B
