import socket

IP = '212.182.24.27'
PORT = 2902

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    liczba_1 = input('podaj pierwsza liczbe: ')
    operator = input('podaj operator: ')
    liczba_2 = input('podaj druga liczbe: ')
    s.sendto(f'{liczba_1}{operator}{liczba_2}'.encode('utf-8'), (IP, PORT))
    data, address = s.recvfrom(1024)
    
print(data.decode('UTF-8'))