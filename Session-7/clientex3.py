import socket

# Create a socket for communicating with the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Always use this parameter!

print("Socket created")

PORT = 8081
IP = "212.128.253.107"
s.connect((IP, PORT))


mess = input("Enter a valid message: ")
s.send((str.encode(mess)))

msg =  s.recv(2048).decode("utf-8")
print("Message from the server")
print(msg)

s.close()

print("The end")