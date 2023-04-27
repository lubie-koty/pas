import socket

HOST = '127.0.0.1'
PORT = 25

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:
        connection, address = s.accept()
        with connection:
            user_authenticated = False
            connection.send(b'220 Welcome to my SMTP server.\r\n')
            while True:
                client_message = connection.recv(1024)
                if client_message == b'QUIT\r\n':
                    connection.send(b'221 Bye\r\n')
                    break
                
                if client_message == b'STARTTLS\r\n':
                    connection.send(b'220 OK\r\n')
                    if connection.recv(1024) == b'AUTH LOGIN\r\n':
                        connection.send(b'334 :)\r\n')
                        connection.recv(1024)
                        connection.send(b'334 :)\r\n')
                        connection.recv(1024)
                        connection.send(b'235 ok auth\r\n')
                        user_authenticated = True
                    else:
                        connection.send(b'404 unknown command\r\n')
                
                if user_authenticated:
                    if 'MAIL FROM:' in client_message.decode():
                        connection.send(b'250 ok\r\n')
                        if 'RCPT TO:' in connection.recv(1024).decode():
                            connection.send(b'250 ok\r\n')
                            if 'DATA' in connection.recv(1024).decode():
                                connection.send(b'354 Start mail input; end with <CRLF>.<CRLF>\r\n')
                                while connection.recv(1024).decode()[-5:] != '\r\n.\r\n':
                                    pass
                                connection.send(b'250 ok\r\n')
                            else:
                                connection.send(b'400 wrong command\r\n')
                        else:
                            connection.send(b'400 wrong command\r\n')
                    else:
                        connection.send(b'404 unknown command\r\n')
                else:
                    connection.send(b'403 error\r\n')
