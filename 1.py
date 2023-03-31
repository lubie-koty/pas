import socket

is_number_not_found = True

HOST = '212.182.24.27'
PORT = 2912

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while is_number_not_found:
        s.sendall(input('podaj liczbe: ').encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print(data)
        if data == 'odgadnieto liczbe :)':
            is_number_not_found = False
