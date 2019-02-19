import socket
import termcolor

PORT = 8081
IP = "212.128.253.105"
MAX_OPEN_REQUEST = 5  # tHIS IS THE MAXIMUM NUMBER OF CLIENTS THE SERVER'LL ACCEPT


def process_client(cs):
    # we receive the message from the client and read it in a "human way" for us to read
    msg = cs.recv(2048).decode("utf-8")

    termcolor.cprint("Message received from tha client: {}".format(msg), 'blue')
    if msg == 'EXIT':
        serversocket.close()

    # With this command we send the message to the client thIs time in BYTES
    # because we are an echo server
    cs.send(str.encode(msg))

    # Close the socket
    cs.close()


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
    process_client(clientsocket)
    # --- Close the socket
    clientsocket.close()
