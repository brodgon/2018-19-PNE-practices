import http.server
import socketserver
import termcolor
from Seq import Seq

# Define the Server's port
PORT = 8085


def validation(seq):
    valid = "ACTG"
    # it will check letter by letter that is one of ACTG
    for letter in seq:
        # if not, an error message will be printed and the program is stopped.
        if letter not in valid:
            return False

    return True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET Received")
        print("Request line" + self.requestline)
        print("     Cnd:  " + self.command)
        print("Path:    " + self.path)

        termcolor.cprint(self.requestline, 'blue')
        if self.path == "/":
            with open("main.html", "r") as c:
                contents = c.read()
        elif "msg" in self.path:
            echo_mess = self.path.split("&")
            sequence = echo_mess[0][echo_mess[0].find("=")+1:]
            validation(sequence)
            if validation(sequence):
                info1 = ""
                info2 = ""
                info3 = ""
                seq = Seq(sequence)
                info1 += "Your sequence is " + sequence

                for i in range(len(echo_mess)):
                    if "chk" in echo_mess[i]:
                        tl = seq.len()
                        info2 += "The total length is " + str(tl) + "\n"
                    elif "base" in echo_mess[i]:
                        b = echo_mess[i].split("=")
                        base = b[1]
                    elif "operation" in echo_mess[i]:
                        op = echo_mess[i].split("=")
                        if op[1]== "perc":
                            perc = seq.perc(base)
                            info3 += "The percentage for base " + base + " is " + str(perc) + "%"
                        elif op[1] == "count":
                            counter = seq.strbases.count(base)
                            info3 += "The number of time your selected base appears is: " + str(counter)


                with open("solution.html","r") as f:
                    contents = f.read().format(info1, info2, info3)
                    f.close()
            else:
                with open("error.html", "r") as c:
                    contents = c.read()
                    c.close()


        # -- We want to generate a response message with the following command
        self.send_response(200)

        # --- Now we will define the content type and the header
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # We now finish the header
        self.end_headers()

        # We will now send the body of the response se message
        self.wfile.write(str.encode(contents))



Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

print("")
print("Server Stopped")
