import socket

HOST = '127.0.0.1'
PORT = 110

messages = [
    b'Subject: wiadomosc 1\r\n\r\nwiadomosc testowa 1.\r\n',
    b'Subject: wiadomosc 2\r\n\r\nwiadomosc testowa 2.\r\n',
    b'Subject: wiadomosc 3\r\n\r\nwiadomosc testowa 3.\r\n'
]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:
        connection, client_address = s.accept()
        print(f'Connection from {client_address}')
        
        with connection:
            connection.send(b'+OK POP3 server ready\r\n')
            while True:
                command = connection.recv(1024).decode().strip()
                if not command:
                    continue
                print(f'Received: {command}')

                if command.startswith('USER'):
                    connection.send(b'+OK\r\n')
                    password_command = connection.recv(1024).decode().strip()
                    if password_command.startswith('PASS'):
                        connection.send(b'+OK\r\n')
                    else:
                        connection.send(b'-ERR unknown command\r\n')
                elif command.startswith('LIST'):
                    response = b'+OK\r\n'
                    for i, message in enumerate(messages):
                        response += f'{i+1} {len(message)}\r\n'.encode()
                    response += b'.\r\n'
                    connection.send(response)
                elif command.startswith('RETR'):
                    message_num = int(command.split()[1])
                    if message_num < 1 or message_num > len(messages):
                        response = b'-ERR message not found\r\n'
                    else:
                        response = b'+OK\r\n'
                        response += messages[message_num-1]
                        response += b'.\r\n'
                    connection.send(response)
                elif command.startswith('QUIT'):
                    response = b'+OK\r\n'
                    connection.send(response)
                    break
                else:
                    response = b'-ERR unknown command\r\n'
                    connection.send(response)
