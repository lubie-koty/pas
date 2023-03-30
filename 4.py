import socket
import operator


operators = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod
}


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
                for op in operators:
                    split_data = data.split(op)
                    if len(split_data) != 1:
                        break

                if len(split_data) == 1:
                    connection.sendall(b'wrong syntax')
                connection.sendall(f'{operators[split_data[1]](int(split_data[0]), int(split_data[2]))}'.encode('utf-8'))
            else:
                print(f'no data received from {client_address}')
