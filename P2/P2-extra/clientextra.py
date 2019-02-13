# we are going to create our client

# We import socket
# we impute the seq object

import socket
from Seq import Seq

# Create a socket for communicating with the server

# We are connecting to the port and the IP of the lab's server (it will change depending on the server)
PORT = 8092
IP = "212.128.253.107"

# Thanks to this loop the client will always ask for a sequence and send the info to the server
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Always use this parameter!
    s.connect((IP, PORT))
    sequ = input("Enter a valid DNA sequence: ")
    s.send(str.encode(sequ))     # Send the info to the server
    msg = s.recv(2048).decode("utf-8")
    print(msg)

    print("\n", "This is the end of the program!")
    s.close()

    print("The end")