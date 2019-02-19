# We are creating a socket from scratch
import socket

PORT = 8081
IP = "212.128.253.105"
MAX_OPEN_REQUEST = 5  # tHIS IS THE MAXIMUM NUMBER OF CLIENTS THE SERVER'LL ACCEPT

# Create a socket for connecting to the clients
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # typical parameters

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))

while True:
    # WE want the server to wait for connections.
    print("Waiting for connections at {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()  # This command will wait and block the server until client connects

    # --- Process the client request
    print("Attending  client: {}".format(address))

    # --- Close the socket
    clientsocket.close()
