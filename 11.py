import socket
import re

regex_pattern_a = 'zad15odpA;ver;(4|6);srcip;(?:[0-9]{1,3}\.){3}[0-9]{1,3};destip;(?:[0-9]{1,3}\.){3}[0-9]{1,3};type;(6|17)'
regex_pattern_b = 'zad15odpB;srcport;\d{1,5};dstport;\d{1,5};data;.+'
IP = '127.0.0.1'
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((IP, PORT))
    
    while True:
        data, address = s.recvfrom(1024)
        data = data.decode('utf-8')
        
        if not re.findall(regex_pattern_a, data):
            s.sendto(b'BAD_SYNTAX', address)
            continue
        
        data = data.split(';')
        if data[2] == '4' and \
           data[4] == '212.182.24.27' and \
           data[6] == '192.168.0.2' and \
           data[8] == '6':
            s.sendto(b'TAK', address)
            while True:
                data_yes, address_yes = s.recvfrom(1024)
                data_yes = data.decode('utf-8')
                if not re.findall(regex_pattern_b, data_yes):
                    s.sendto(b'BAD_SYNTAX', address_yes)
                    break
                
                if data_yes[2] == '2900' and \
                   data_yes[4] == '47526' and \
                   data_yes[6] == 'network programming is fun':
                    s.sendto(b'TAK', address_yes)
                else:
                    s.sendto(b'NIE', address_yes)
                break

        else:
            s.sendto(b'NIE', address)
