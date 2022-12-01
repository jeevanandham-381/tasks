from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "192.168.1.110"
PORT = 7777

class NewHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("comtent-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("demo.html", "utf-8"))

server = HTTPServer((HOST,PORT),(NewHTTP))
print("server running ")
server.serve_forever()
server.server_close()
print("server stopped")




