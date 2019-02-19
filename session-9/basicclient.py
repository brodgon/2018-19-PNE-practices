import socket

# SERVER IP, PORT
PORT = 8081
IP = "212.128.253.105"
# Create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Close the socket
s.close()
