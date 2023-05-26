import logging
import socket
import threading


class Server:
    def __init__(self, ip_address, port, log_file):
        self.ip_address = ip_address
        self.port = port
        self.server_socket = None
        self.logger = self.start_logger(log_file)

    def start_logger(self, log_file):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        logger.addHandler(
            logging.FileHandler(log_file).setFormatter(
                logging.Formatter('%(name)s :: %(levelname)-8s :: %(asctime)s :: %(message)s')
            )
        )
        return logger

    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.ip_address, self.port))
        self.server_socket.listen()
        self.logger.info(f'Listening on {self.ip_address}:{self.port}...')

        while True:
            connection, address = self.server_socket.accept()
            self.logger.info(f'Client connection: {address[0]}:{address[1]}')
            thread = threading.Thread(target=self.handle_session, args=[connection])
            thread.start()


    def handle_session(self, connection):
        self.logger.info('Starting connection with a client...')
        with connection:
            while True:
                data = connection.recv(1024)
                self.logger.info(f'Received data: {data}')
                if not data:
                    self.logger.info('Ending connection with a client...')
                    break
                connection.sendall(data)
                self.logger.info(f'Sending data: {data}')


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 2115
    FILE_NAME = 'logi_serwera.log'
    server = Server(HOST, PORT, FILE_NAME)
    server.start_server()
