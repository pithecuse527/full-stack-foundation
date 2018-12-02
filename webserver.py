from BaseHTTPServer import BaseHTTPRequestHandler, BaseHTTPServer

class webserverhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endwith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')

                output = ""
                output += "<html><body>Hello!</body></html>"
                self.write.write(output)
                print output
                return

        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverhandler)
        print "We server running on port %s" % port
        server.serve_forever()

    except KeyboardInterrupt:       # when user holds Ctrl+C
        print "^C entered, stopping web server..."
        server.socket.close()


if __name__ == '__main__':
    main()
