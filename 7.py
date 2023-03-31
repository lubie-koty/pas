import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('212.182.24.27', 2900))
    while True:
        try:
            s.sendall(b'wiadomosc')
            print(s.recv(1024).decode('UTF-8'))
        except KeyboardInterrupt:
            print('zakonczono program')
            break