import socket
import threading

HEADER = 64    #64 bytes
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())   # gets my laptop IP address
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # we created a socket, picked a type and picked the method
server.bind(ADDR)

def handle_client(conn, addr):     # this funtion handles all the communication between the client and surver
    print("[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)    # decode measn decode the message from it's from its bytes format into a string using utf-8
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Message received".encode(FORMAT))       
    conn.close()

def start():
    server.listen()   # we're now listening for new connections
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, ADDR = server.accept()
        #msg_length = conn.recv(HEADER).decode(FORMAT)     # conn is a socket object that allows us to communicate back to the thing that connected to our server
        thread = threading.Thread(target=handle_client, args=(conn,addr)) # all the connections made are passed to the the handle_client function
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") # tells us the number of connections, each thread represents the a client connection

print("[STARTING] server is starting...")
start()