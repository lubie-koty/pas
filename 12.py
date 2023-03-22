import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('212.182.24.27', 2908))
    
    message = input('podaj wiadomosc: ')
    if len(message) > 20:
        message = message[:19]
    elif len(message) < 20:
        while len(message) != 20:
            message += ' '
    message = message.encode('utf-8')
    len_message = len(message)

    total_sent_data = 0
    while total_sent_data < len_message:
        sent_data = s.send(message[total_sent_data:])
        if sent_data == 0:
            continue
        total_sent_data += sent_data
        
    data = []
    total_received_data = 0
    while total_received_data < len_message:
        received_data = s.recv(min(len_message - total_received_data, 1024))
        if received_data == b'':
            continue
        data.append(received_data)
        total_received_data += len(received_data)
    

print(b''.join(data).decode('UTF-8'))
