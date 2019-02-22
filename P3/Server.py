"""We are creating the server which calculate functions of a sequence introduced by a user in the client"""
import socket
from Seq import Seq

PORT = 8098
IP = "192.168.56.1"
MAX_OPEN_REQUEST = 5

# First we are defining functions

# Process_client will hold most operations


def process_client(cs):
    # we receive the message from the client and read it in a "human way".
    mess = cs.recv(2048).decode("utf-8")
    # First we work on the message content:
    # if the message is empty (in our case " ") we will automatically respond the user
    if mess == " ":
        msg = "I'M ALIVE!"
        cs.send(str.encode(msg))
    # if the message is not empty it will enter this clause (else)
    else:
        # ---We create an empty variable for keeping the answers and create a list with the requests of the user
        #    separating it by "\n" ---
        msg = ""  # empty for the message
        rlist = mess.split("\n")
        seq = rlist[0].upper()   # we transform any sequence in capital letters (sequences are keep on the first item)
        # We call validation() --- explained later when defined---
        validation(seq)
        # if the function returns true
        if validation(seq):
            # we add to our message that the sequence selected was OK
            msg += "OK! Valid sequence."+"\n"
            # Transform the sequence to an object to make operations
            seq1 = Seq(seq)
            # Eliminate the first element of the list (sequence) for us to iterate over it
            # we also eliminate the last element, which is nothing (generated always by default)
            rlist.pop(0)
            rlist.pop()  # this function without argument eliminate the last element
            # Now we iterate over the list and check if the functions requested by the user are possible to handle
            # if they are the information will be keep in msg, if not, an error message will be keep
            for i in range(len(rlist)):
                if rlist[i] == "len":
                    tl = seq1.len()
                    msg += "The total length is "+str(tl)+"\n"
                elif rlist[i] == "complement":
                    comp = seq1.complement()
                    msg += "The complement sequence for the introduced one is:"+comp+"\n"
                elif rlist[i] == "reverse":
                    rev = seq1.reverse()
                    msg += "The reversed sequence for the introduced one is:" + rev + "\n"
                elif rlist[i] == "countA":
                    counter = seq1.strbases.count("A")
                    msg += "The number of As in your sequence is:" + str(counter) + "\n"
                elif rlist[i] == "countT":
                    counter = seq1.strbases.count("T")
                    msg += "The number of Ts in your sequence is:" + str(counter) + "\n"
                elif rlist[i] == "countG":
                    counter = seq1.strbases.count("G")
                    msg += "The number of Gs in your sequence is:" + str(counter) + "\n"
                elif rlist[i] == "countC":
                    counter = seq1.strbases.count("C")
                    msg += "The number of Cs in your sequence is:" + str(counter) + "\n"
                elif rlist[i] == "percA":
                    perc = seq1.perc("A")
                    msg += "The percentage of As in your sequence is:" + str(perc) + "%" + "\n"
                elif rlist[i] == "percT":
                    perc = seq1.perc("T")
                    msg += "The percentage of Ts in your sequence is:" + str(perc) + "%" + "\n"
                elif rlist[i] == "percG":
                    perc = seq1.perc("G")
                    msg += "The percentage of Gs in your sequence is:" + str(perc) + "%" + "\n"
                elif rlist[i] == "percC":
                    perc = seq1.perc("C")
                    msg += "The percentage of Cs in your sequence is:" + str(perc) + "%" + "\n"
                else:  # operation is not registered or misspelled.
                    msg += "ERROR! This operation " + rlist[i] + " cannot be held."

            # Once we finished iterating the message will be send to the client
            cs.send(str.encode(msg))


# function (validation)  will ensure that the sequence introduced is correct.


def validation(seq):
    valid = "ACTG"
    # it will check letter by letter that is one of ACTG
    for letter in seq:
        # if not, an error message will be printed and the program is stopped.
        if letter not in valid:
            msg = "Letter " + letter + " not valid." + "\n"
            clientsocket.send(str.encode(msg))
            return False
    return True


# Create a socket for connecting to the clients
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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

