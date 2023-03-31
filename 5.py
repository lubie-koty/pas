import socket

IP = '212.182.24.27'
PORT = 2901

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    while True:
        try:
            s.sendto(input('podaj wiadomosc: ').encode('utf-8'), (IP, PORT))
            data, address = s.recvfrom(1024)
            print(data.decode('utf-8'))
        except KeyboardInterrupt:
            print('zakonczono program')
            break
