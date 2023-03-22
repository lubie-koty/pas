import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('212.182.24.27', 2908))
    
    message = input('podaj wiadomosc: ')
    if len(message) > 20:
        message = message[:19]
    elif len(message) < 20:
        while len(message) != 20:
            message += ' '

    s.sendall(message.encode('utf-8'))
    data = s.recv(1024)
    
print(data.decode('UTF-8'))