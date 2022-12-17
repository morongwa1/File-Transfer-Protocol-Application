import socket
import threading

HEADER = 2048    #2048 bytes
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())   
server_addr = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "EXIT"

ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSocket.bind(server_addr)

def threaded_client(conn,addr):
    while True:
        client_data = conn.recv(HEADER).decode(FORMAT)
        print(f"Server received: {client_data}")
        conn.send(client_data.encode(FORMAT))
        
        if client_data == DISCONNECT_MESSAGE:
            print(f"No more data received from {client_data}")
            break
        print("Sending received message back to the client")
        conn.send("Message received".encode(FORMAT))
    print("Closing socket")
    conn.close()

def start():
    print("Waiting for a connection")
    ServerSocket.listen(5)
    while True:
        # Wait for a connection
        conn, server_addr = ServerSocket.accept()
        print(f"connection from: {server_addr}")
        # start_new_thread(threaded_client, (conn, ))
        # all the connections made are passed to the the handle_client function
        thread = threading.Thread(target=threaded_client, args=(conn,server_addr)) 
        thread.start()
        # tells us the number of connections, each thread represents the a client connection
        print(f"[ACTIVE CONNECTIONS] : {threading.activeCount() - 1}")
start()
