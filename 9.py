import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(input('ip address: ').encode('utf-8'), ('212.182.24.27', 2906))
    data, address = s.recvfrom(1024)
    
print(f'hostname: {data.decode("utf-8")}')
