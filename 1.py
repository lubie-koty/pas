import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('ntp.task.gda.pl', 13))
    data = s.recv(1024)
    
print(data.decode('UTF-8'))