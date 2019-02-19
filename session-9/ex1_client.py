import socket

# SERVER IP, PORT
IP = "212.128.253.105"
PORT = 8081

while True:
    msg = input("Insert a message for the server")

    # if the following two commands are before the message, the client will connect and wait for the message
    # making the server busy and blocking it

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers response
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response- 'Message from the server' : {}".format(response))

    s.close()