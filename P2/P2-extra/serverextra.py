import socket
from Seq import Seq   # We are importing seq object
# Configure the Server's IP and PORT
PORT = 8092
IP = "212.128.253.107"
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        # Another connection!e
        number_con += 1

        # Print the conection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the message from the client, if any
        msg = clientsocket.recv(2048).decode("utf-8")
        print("Message from client: {}".format(msg))

        # Send the messag
        message = "Welcome to my server!! :)"+"\n"
        seq = Seq(msg) # Transform into object
        seq1="This is the complement sequence for your sequence: "+seq.complement()    # Calculate complement
        send_bytes = str.encode(message)
        send_comp = str.encode(seq1)  # Encode the complement
        # We must write bytes, not a string
        clientsocket.send(send_bytes)
        clientsocket.send(send_comp)
    clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()