import socket

HEADER = 2048    #20148 bytes
PORT = 12345
SERVER = socket.gethostbyname(socket.gethostname())   # gets my laptop IP address
server_addr = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "EXIT"

# Create a UDP socket
ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # taking message from user
    msg = input("Enter your message: ")
    if msg != DISCONNECT_MESSAGE:      
        print(f"sending {msg}")
        # Send data to server
        ClientSocket.sendto(msg.encode(FORMAT),(SERVER, PORT))
        # Look for the response
        serve_data,addr = ClientSocket.recvfrom(HEADER)
        # Print the received message
        print(f"received from server:  {serve_data}")
    else:
        print("DONE!!!")
        break

ClientSocket.sendto(DISCONNECT_MESSAGE.encode(FORMAT),server_addr)

print("closing socket")
ClientSocket.close()
