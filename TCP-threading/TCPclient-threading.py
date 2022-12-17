import socket

HEADER = 2048    
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())   
server_addr = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "EXIT"

ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientSocket.connect(server_addr)

print("Waiting for connection")

try:
    while True:
        # taking message from user
        msg = input("Enter your message: ")
        if msg != DISCONNECT_MESSAGE:
            # Send data to server
            ClientSocket.send(msg.encode(FORMAT))
            serve_data = ClientSocket.recv(HEADER).decode(FORMAT)
            print(f"received from server:  {serve_data}")
        else:
            print("DONE!!!")
            break

    ClientSocket.send(DISCONNECT_MESSAGE.encode(FORMAT))
finally:
    print("closing socket")
    ClientSocket.close()

