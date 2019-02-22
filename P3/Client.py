"""We are creating a client which ask the user for a DNA sequence and some function(s)"""
import socket

PORT = 8098
IP = "192.168.56.1"

while True:
    # We create an empty variable in order to keep the input information
    request = ""
    # We create an infinite loop which will ask the user for information until a specific parameter is introduced
    while True:
        inp = input("*")+"\n"
        # if there exist some information on the input it will be stored in request
        if inp and inp.strip():
            request += inp
        # if the input is empty (the user press intro when it is asked) the loop will finish
        else:
            break
    # Here were dealing with an specific case:
    # If the first time the user is asked he/she press intro nothing will be stored in request
    # so the length will be 0. We have to transform that into a "secret message" which has length
    # otherwise, it is impossible to send something.
    if len(request) == 0:
        request = " "

    # Once we have all the information we connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    # We send the information
    s.send(str.encode(request))

    # We receive message from the server and print it
    msg = s.recv(2048).decode("utf-8")
    print(msg)
    # ----Close the socket----
    s.close()

