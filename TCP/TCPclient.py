import socket

HEADER = 2048    #2048 bytes
PORT = 5050   #Port to listen on
SERVER = socket.gethostbyname(socket.gethostname())   # gets local IP address
server_addr = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "EXIT"

# Create a TCP socket
ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
ClientSocket.connect(server_addr)

try:
    while True:
        # taking message from user
        msg = input("Enter your message: ")
        if msg != DISCONNECT_MESSAGE:
            # Send data to server
            ClientSocket.send(msg.encode(FORMAT))
            # Look for the response
            serve_data = ClientSocket.recv(HEADER).decode(FORMAT)
            print(f"received from server:  {serve_data}")
        else:
            print("DONE!!!")
            break

    ClientSocket.send(DISCONNECT_MESSAGE.encode(FORMAT))
finally:
    print("closing socket")
    ClientSocket.close()
