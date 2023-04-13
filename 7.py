import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('212.182.24.27', 2900))
    s.listen()
    
    while True:
        connection, client_address = s.accept()
        with connection:
            data = connection.recv(1024)
            data = data.decode('utf-8')
            if len(data) > 20:
                connection.sendall(b'za dluga wiadomosc')
            else:
                connection.sendall(data.encode('utf-8'))
        