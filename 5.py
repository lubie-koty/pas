import socket


IP = '127.0.0.1'
PORT = 6666


print(f'starting up on {IP}:{PORT}')
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((IP, PORT))
    s.listen()
    
    while True:
        connection, client_address = s.accept()
        with connection:
            print(f'connection from {client_address}')
            data = connection.recv(1024).decode('utf-8')
            if data:
                connection.sendall(f'{socket.gethostbyaddr(data)[0]}'.encode('utf-8'))
            else:
                print(f'no data received from {client_address}')
