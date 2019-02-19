import socket
from Seq import Seq

PORT = 8081
IP = "192.168.1.40"
MAX_OPEN_REQUEST = 5


def process_client(cs):
    # we receive the message from the client and read it in a "human way" for us to read
    mess = cs.recv(2048).decode("utf-8")

    if mess == "":
        msg = "ALIVE"
        cs.send(str.encode(msg))
    else:
        seq = Seq(mess)
        msg = "We are going to work with the following sequence: "+mess
        cs.send(str.encode(msg))
        request = cs.recv(2048).decode("utf-8")
        if request == 'len':
            tl = seq.len()
            msg1 = "Total length of the sequence introduced is "+str(tl)
            cs.send(str.encode(msg1))


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

