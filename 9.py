import socket
import re

regex_pattern = 'zad13odp;src;\d{1,5};dst;\d{1,5};data;.+'
IP = '127.0.0.1'
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((IP, PORT))
    
    while True:
        data, address = s.recvfrom(1024)
        data = data.decode('utf-8')
        
        if not re.findall(regex_pattern, data):
            s.sendto(b'BAD_SYNTAX', address)
            continue
        
        data = data.split(';')
        if data[2] == '' and \
           data[4] == '' and \
           data[6] == 'siema':
            s.sendto(b'TAK', address)
        else:
            s.sendto(b'NIE', address)
