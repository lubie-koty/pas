import socket

IP = '212.182.24.27'
PORT = 2901

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b'wiadomosc', (IP, PORT))
    data, address = s.recvfrom(1024)
    
print(data.decode('UTF-8'))