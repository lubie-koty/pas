import socket
import re

IP = '212.182.24.27'
TARGET_PORT = 2913
count_pongs = 0

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.settimeout(2)
    for port in range(666, 65536):
        if count_pongs == 3:
            break
        if re.findall('.+666', str(port)):
            s.sendto(b'PING', (IP, port))
            data, address = s.recvfrom(1024)
            if data:
                data = data.decode('utf-8')
                if data == 'PONG':
                    count_pongs += 1

if count_pongs == 3:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_tcp:
        s_tcp.connect((IP, TARGET_PORT))
        s_tcp.sendall(b'asdf')
        data = s_tcp.recv(1024)
        print(data.decode('utf-8'))