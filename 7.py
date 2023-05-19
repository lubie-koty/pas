from http.server import BaseHTTPRequestHandler, HTTPServer

IP = '127.0.0.1'
PORT = 15


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = 'Hello, world!'
            self.wfile.write(bytes(message, 'utf8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = 'Not found.'
            self.wfile.write(bytes(message, 'utf8'))


server_address = (IP, PORT)
httpd = HTTPServer(server_address, MyHTTPRequestHandler)
print(f'Starting server on {IP}:{PORT}...')
httpd.serve_forever()
