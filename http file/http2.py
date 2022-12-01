from http.server import HTTPServer,BaseHTTPRequestHandler

class echoHandler(BaseHTTPRequestHandler):    #echoHandler request handler
    def do_GET(self):
        self.send_response(200)     # we are looking on the server is found and will be displayed on the web page.
        self.send_header("content-type", 'text/html')   #sending header info
        self.end_headers()
        self.wfile.write("name:jeeva".encode())   #http servers cannot send string on the http request,(encode)


def main():
    PORT = 5555
    server=HTTPServer(('',PORT),echoHandler)    #hold the instance of server
    print('server running on port %s' %PORT)
    server.serve_forever()    #start the server
    server.server_close()


if __name__=='__main__':       #that this file is running directly and we haven’t imported
    main()

