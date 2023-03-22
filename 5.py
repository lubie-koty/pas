import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect(('212.182.24.27', 2901))
    while True:
        try:
            s.sendall(input('podaj wiadomosc: ').encode('utf-8'))
            print(s.recv(1024).decode('UTF-8'))
        except KeyboardInterrupt:
            print('zakonczono program')
            break
