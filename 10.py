import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(input('hostname: ').encode('utf-8'), ('212.182.24.27', 2906))
    data = s.recvfrom(1024)
    
print(f'ip address: {data.decode("utf-8")}')
