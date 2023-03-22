import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect(('212.182.24.27', 2906))
    s.sendall(input('hostname: ').encode('utf-8'))
    data = s.recv(1024)
    
print(f'ip address: {data.decode("utf-8")}')
