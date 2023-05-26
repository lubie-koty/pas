import logging
import random
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
            thread = threading.Thread(target=self.handle_session, args=[connection, random.randint(1, 100)])
            thread.start()


    def handle_session(self, connection, secret_number: int):
        self.logger.info(f'Starting connection with a client - secret number: {secret_number}...')
        with connection:
            while True:
                data = connection.recv(1024)
                self.logger.info(f'Received data: {data}')
                if not data:
                    break
                try:
                    guessed_number = int(data.decode())
                except ValueError:
                    connection.sendall(b'Entered value is not an integer...')
                if guessed_number < secret_number:
                    connection.sendall(b'Secret number is larger...')
                elif guessed_number > secret_number:
                    connection.sendall(b'Secret number is smaller...')
                else:
                    connection.sendall(b'You guessed right!')
                    break
            self.logger.info('Ending connection with a client...')


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 2115
    FILE_NAME = 'logi_serwera.log'
    server = Server(HOST, PORT, FILE_NAME)
    server.start_server()
