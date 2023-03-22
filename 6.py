import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect(('212.182.24.27', 2902))
    liczba_1 = input('podaj pierwsza liczbe: ')
    operator = input('podaj operator: ')
    liczba_2 = input('podaj druga liczbe: ')
    s.sendall(f'{liczba_1}{operator}{liczba_2}'.encode('utf-8'))
    data = s.recv(1024)
    
print(data.decode('UTF-8'))