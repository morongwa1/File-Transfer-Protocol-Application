import socket
import threading

HEADER = 2048    
PORT = 12345
SERVER = socket.gethostbyname(socket.gethostname())  
server_addr = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "EXIT"

ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def threaded_client(data,addr):
    print(f"Server received: {data}")
    print("Sending received message back to the client")
    ServerSocket.sendto(data.encode(FORMAT),addr)
          
def start():
    ServerSocket.bind(server_addr)
    print("Waiting for a connection")
    while True:
        # Wait for a connection
        client_data,client_addr = ServerSocket.recvfrom(HEADER)
        message = client_data.decode(FORMAT)
        if message == DISCONNECT_MESSAGE:
            print(f"No more data received from {message}")
            print("Closing socket")
            ServerSocket.close()
            break
        # all the connections made are passed to the the handle_client function
        thread = threading.Thread(target=threaded_client, args=(message, client_addr)) 
        thread.start()
        # tells us the number of connections, each thread represents the a client connection
        print(f"[ACTIVE CONNECTIONS] : {threading.activeCount() - 1}") 
start()
