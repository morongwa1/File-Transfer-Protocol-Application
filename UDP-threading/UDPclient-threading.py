import socket

HEADER = 2048    #64 bytes
PORT = 12345
SERVER = socket.gethostbyname(socket.gethostname())   # gets my laptop IP address
server_addr = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "EXIT"

ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:
    # taking message from user
    msg = input("Enter your message: ")
    client_message = msg.encode(FORMAT)
    if msg != DISCONNECT_MESSAGE:   
        # Send data to server
        ClientSocket.sendto(client_message,(SERVER, PORT))
        serve_data, addr = ClientSocket.recvfrom(HEADER)
        server_message = serve_data.decode(FORMAT)
        print(f"received from server:  {server_message}")
    else:
        print("DONE!!!")
        break
    
ClientSocket.sendto(DISCONNECT_MESSAGE.encode(FORMAT),(SERVER, PORT))

print("closing socket")
ClientSocket.close()

