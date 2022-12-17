import socket
HEADER = 2048    #2048 bytes
PORT = 12345
SERVER = socket.gethostbyname(socket.gethostname())   # gets my laptop IP address
server_addr = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "EXIT"

# Create a UDPsocket
ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
print(f"Starting up on {server_addr}")
ServerSocket.bind((SERVER,PORT))

# Receive the data from the client in small chunks and resend it back to the client
while True:
    print("waiting for client....")
    client_data,client_addr = ServerSocket.recvfrom(HEADER)
    print(f"Server received: {client_data} from client")
    if client_data.decode(FORMAT) != DISCONNECT_MESSAGE:
        print("Sending received message back to the client")
        ServerSocket.sendto(client_data,client_addr)
    else:
        print(f"No more data received from {client_addr}")
        break
            
# Clean up the connection
print("closing socket")
ServerSocket.close()