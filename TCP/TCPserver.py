import socket

HEADER = 2048    # 2048 bytes
PORT = 5050        # The port to listen on
SERVER = socket.gethostbyname(socket.gethostname())   # gets my laptop IP address
server_addr = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "EXIT"

# Create a TCPsocket
ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
print(f"Starting up on {server_addr}")
ServerSocket.bind(server_addr)

# Listen for incoming connections
ServerSocket.listen(1)

while True:
    # Wait for a connection
    print("Waiting for a connection")
    conn, client_addr = ServerSocket.accept()

    try:
        print(f"connection from: {client_addr}")

        # Receive the data from the client in small chunks and resend it back to the client
        while True:
            client_data = conn.recv(HEADER).decode(FORMAT)
            print(f"Server received: {client_data} from client")
            if client_data != DISCONNECT_MESSAGE:
                print("Sending received message back to the client")
                conn.send(client_data.encode(FORMAT))
            else:
                print(f"No more data received from {client_addr}")
                break
            
    finally:
        # Clean up the connection
        print("closing socket")
        conn.close()