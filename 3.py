import socket


IP = '127.0.0.1'
PORT = 6666


print(f'starting up on {IP}:{PORT}')
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((IP, PORT))
    
    while True:
        data, client_address = s.recvfrom(1024)
        print(f'connection from {client_address}')
        s.sendto(data, client_address)
