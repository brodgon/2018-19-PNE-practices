import socket


PORT = 8098
IP = "212.128.253.106"


while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

    request = ""
    while True:
        inp = input()+"\n"
        if inp and inp.strip():
            request += inp
        else:
            break

    if len(request) == 0:
        request = " "

    s.send(str.encode(request))

    msg = s.recv(2048).decode("utf-8")
    print(msg)
    print("\n", "This is the end of the program!")
    s.close()

    print("The end")

