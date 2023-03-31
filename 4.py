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
    
    while True:
        data, client_address = s.recvfrom(1024)
        print(f'connection from {client_address}')
        data = data.decode('utf-8')

        for op in operators:
            split_data = data.split(op)
            if len(split_data) != 1:
                break
        if len(split_data) == 1:
            s.sendto(b'wrong syntax', client_address)

        s.sendto(f'{operators[split_data[1]](int(split_data[0]), int(split_data[2]))}'.encode('utf-8'), client_address)
