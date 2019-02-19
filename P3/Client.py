import socket

# Create a socket for communicating with the server

# We are connecting to the port and the IP of the lab's server (it will change depending on the server)
PORT = 8081
IP = "192.168.1.40"

# Thanks to this loop the client will always ask for a sequence and send the info to the server
while True:
    sequ = input("Enter a valid DNA sequence: ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Always use this parameter!
    s.connect((IP, PORT))
    s.send(str.encode(sequ))
    msg = s.recv(2048).decode("utf-8")
    if msg == 'ALIVE':
        print(msg)
    else:
        requests = input("What operations do you want to hold? ")
        s.send(str.encode(requests))
        msg1 = s.recv(2048).decode("utf-8")
        print(msg1)

    print("\n", "This is the end of the program!")
    s.close()

    print("The end")
