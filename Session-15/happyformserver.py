import http.server
import socketserver
import termcolor

PORT = 8050


class TestHandler(http.server.BaseHTTPRequestHandler):


    def do_GET(self):

        # - - - print the request line
        termcolor.cprint(self.requestline, 'red')

        f = open("form2inputs.html", 'r')
        contents = f.read()

        # -- We want to generate a response message with the following command
        self.send_response(200)

        # --- Now we will define the content type and the header
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # We now finish the header
        self.end_headers()

        # We will now send the body of the response se message
        self.wfile.write(str.encode(contents))

# - - - Start the main program


with socketserver.TCPServer(("",PORT), TestHandler) as httpd:
    print("Serving at port {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

    print("")
    print("Server Stopped")

