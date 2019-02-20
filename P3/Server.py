import socket
from Seq import Seq

PORT = 8095
IP =  "212.128.253.106"
MAX_OPEN_REQUEST = 5


def process_client(cs):
    # we receive the message from the client and read it in a "human way" for us to read
    mess = cs.recv(2048).decode("utf-8")
    print(mess)
    if mess == " ":
        msg = "ALIVE"
        print(msg)
        cs.send(str.encode(msg))
    else:
        hello = mess.split("\n")
        print(hello)
        seq1 = Seq(hello[0])
        for i in range(len(hello)):
            if hello[i] == "len":
                tl = seq1.len()
                msg = "The total length is "+str(tl)
                cs.send(str.encode(msg))




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

