# we are going to create our client

# We import socket
# we impute the seq object

import socket
from Seq import Seq

# Create a socket for communicating with the server

# We are connecting to the port and the IP of the lab's server (it will change depending on the server)
PORT = 8083
IP = "212.128.253.107"

# Thanks to this loop the client will always ask for a sequence and send the info to the server
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Always use this parameter!
    s.connect((IP, PORT))
    sequ = input("Enter a valid DNA sequence: ")
    seq = Seq(sequ)      # Transform str to an obj
    seq1 = seq.complement()   # Calculate inverse and complement
    seq2 = seq.reverse()

    mess1 = "\n"+"The complement sequence is "+seq1
    mess2 = "\n"+"The reverse sequence is "+seq2

    s.send(str.encode(mess1))     # Change to a language that the server understands and send the info
    s.send(str.encode(mess2))

    msg = s.recv(2048).decode("utf-8")
    print(msg)

    print("\n", "This is the end of the program!")
    s.close()

    print("The end")
