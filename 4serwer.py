import socket

HOST = '127.0.0.5'
PORT = 10000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    
    connection, address = s.accept()
    with connection:
        received_data = connection.recv(1024)
        connection.sendall(received_data)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    while True:
        message, address = s.recvfrom(1024)
        s.sendto(message, address)
        break
