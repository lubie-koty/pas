import socket


IP = '127.0.0.1'
PORT = 6666


print(f'starting up on {IP}:{PORT}')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP, PORT))
    s.listen()
    
    while True:
        connection, client_address = s.accept()
        with connection:
            print(f'connection from {client_address}')
            data_chunks = []
            while True:
                data = connection.recv(1024)
                if data:
                    data_chunks.append(data)
                else:
                    print(f'no more data from {client_address}')
                    print('sending received data...')
                    connection.sendall(b''.join(data_chunks))
