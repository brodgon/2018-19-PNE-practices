import socket
from Seq import Seq

PORT = 8098
IP =  "212.128.253.106"
MAX_OPEN_REQUEST = 5


def process_client(cs):
    # we receive the message from the client and read it in a "human way" for us to read
    mess = cs.recv(2048).decode("utf-8")
    print(mess)
    if mess == " ":
        msg = "ALIVE"
        cs.send(str.encode(msg))
    else:
        rlist = mess.split("\n")
        seq = rlist[0].upper()
        validation(seq)
        if validation(seq):
            seq1 = Seq(seq)
            rlist.pop(0)
            for i in range(len(rlist)):
                if rlist[i] == "len":
                    tl = seq1.len()
                    msg = "The total length is "+str(tl)+"\n"
                    cs.send(str.encode(msg))
                elif rlist[i] == "complement":
                    comp = seq1.complement()
                    msg = "The complement sequence for the introduced one is:"+comp+"\n"
                    cs.send(str.encode(msg))
                elif rlist[i] == "reverse":
                    rev = seq1.reverse()
                    msg = "The reversed sequence for the introduced one is:" + rev + "\n"
                    cs.send(str.encode(msg))
                elif rlist[i] == "countA":
                    counter = seq1.strbases.count("A")
                    msg = "The number of As in your sequence is:" + str(counter) + "\n"
                    cs.send(str.encode(msg))
                elif rlist[i] == "countT":
                    counter = seq1.strbases.count("T")
                    msg = "The number of Ts in your sequence is:" + str(counter) + "\n"
                    cs.send(str.encode(msg))
                elif rlist[i] == "countG":
                    counter = seq1.strbases.count("G")
                    msg = "The number of Gs in your sequence is:" + str(counter) + "\n"
                    cs.send(str.encode(msg))
                elif rlist[i] == "countC":
                    counter = seq1.strbases.count("C")
                    msg = "The number of Cs in your sequence is:" + str(counter) + "\n"
                    cs.send(str.encode(msg))
                elif rlist[i] == "percA":
                    perc = seq1.strbases.perc("A")
                    msg = "The percentage of Cs in your sequence is:" + str(perc) + "\n"
                    cs.send(str.encode(msg))
                elif rlist[i] == "percT":
                    perc = seq1.strbases.perc("T")
                    msg = "The percentage of Ts in your sequence is:" + str(perc) + "\n"
                    cs.send(str.encode(msg))
                elif rlist[i] == "percG":
                    perc = seq1.strbases.perc("G")
                    msg = "The percentage of Gs in your sequence is:" + str(perc) + "\n"
                    cs.send(str.encode(msg))
                elif rlist[i] == "percC":
                    perc = seq1.strbases.perc("C")
                    msg = "The percentage of Cs in your sequence is:" + str(perc) + "\n"
                    cs.send(str.encode(msg))
                elif rlist[i] == '':
                    pass
                else:
                    msg = "ERROR! This operation cannot be held"
                    cs.send(str.encode(msg))


def validation(seq):
    valid = "ACTG"
    for letter in seq:
        if letter not in valid:
            MSG = "Letter " + letter + " not valid." + "\n"
            clientsocket.send(str.encode(MSG))
            return False
    return True


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

