import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect(('212.182.24.27', 2901))
    s.sendall(b'witam')
    data = s.recv(1024)
    
print(data.decode('UTF-8'))