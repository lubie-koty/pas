import socket
from time import process_time

HOST = '127.0.0.6'
PORT = 10000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    t_start = process_time()
    s.sendall(b'fajna wiadomosc wow')
    s.recv(1024)
    t_end = process_time()
    print(f'dlugosc przesylu pakietu TCP: {t_end - t_start}')

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((HOST, PORT))
    t_start = process_time()
    s.sendall(b'fajna wiadomosc wow')
    s.recv(1024)
    t_end = process_time()
    print(f'dlugosc przesylu pakietu UDP: {t_end - t_start}')
