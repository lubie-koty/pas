import socket
import threading


class Server:
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.server_socket = None
        
    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.ip_address, self.port))
        self.server_socket.listen()
        
        while True:
            connection, address = self.server_socket.accept()
            thread = threading.Thread(target=self.handle_session, args=[connection])
            thread.start()
            
    
    def handle_session(self, connection):
        with connection:
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                connection.sendall(data)


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 2115
    server = Server(HOST, PORT)
    server.start_server()
