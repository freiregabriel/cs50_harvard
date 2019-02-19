from http.server import BaseHTTPRequestHandler, HTTPServer
port = 8080
server_address = ("0.0.0.0", port)
class HTTPServer_RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        self.wfile.write(b"<!DOCTYPE html>")
        self.wfile.write(b"<html lang='en'>")
        self.wfile.write(b"<head>")
        self.wfile.write(b"<title> Hello, title </title>")
        self.wfile.write(b"</head>")
        self.wfile.write(b"<body>")
        self.wfile.write(b"Hello, World")
        self.wfile.write(b"</body>")
        self.wfile.write(b"</html>")
http_server = HTTPServer(server_address, HTTPServer_RequestHandler)
http_server.serve_forever()