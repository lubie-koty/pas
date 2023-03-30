import socket
from datetime import datetime


def get_time():
	return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


IP = '127.0.0.1'
PORT = 6666


print(f'starting up on {IP}:{PORT}')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP, PORT))
    s.listen()
    
    while True:
        connection, client_address = s.accept()
        with connection:
            print(f'connection from {client_address}')
            data = connection.recv(1024)
            while data:
                t = get_time()
                print(f'sending time to client: {t}')
                connection.sendall(t)
                data = connection.recv(1024)
            print(f'no more data from {client_address}')
