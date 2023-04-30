import socket

# Define the server host and port number
HOST = 'localhost'
PORT = 143

# Create a dictionary of email messages
messages = {
    '1': {
        'from': 'fajny_gosc@wp.pl',
        'to': 'jego_kumpel@wp.pl',
        'subject': 'hejka',
        'body': 'hej,\npamietaj o kolosie za tydzien.'
    },
    '2': {
        'from': 'fajny_gosc@wp.pl',
        'to': 'jego_kumpel@wp.pl',
        'subject': 'narka',
        'body': 'hej,\na i jeszcze nie zapomnij mi oddac 2 zl.'
    },
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:
        connection, address = s.accept()
        print(f'Connected by {address}')

        connection.sendall(b'* OK IMAP4rev1 Service Ready\r\n')
        with connection:
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                tokens = data.decode().split()

                if tokens[0].upper() == 'LOGIN':
                    username = tokens[1]
                    password = tokens[2]
                    if len(tokens) >= 2 and username and password:
                        connection.sendall(b'* OK LOGIN successful\r\n')
                    else:
                        connection.sendall(b'* NO LOGIN failed\r\n')

                elif tokens[0].upper() == 'LIST':
                    connection.sendall(b'* LIST () "/" "INBOX"\r\n')

                elif tokens[0].upper() == 'FETCH':
                    message_id = tokens[1].strip('{}')

                    if message_id in messages:
                        message = messages[message_id]
                        connection.sendall('''
                            * 1 FETCH (UID 1 FLAGS () INTERNALDATE "01-Jan-2023 00:00:00 +0000" RFC822.SIZE 50 ENVELOPE 
                            ("{0}" "{1}" "{2}")
                            BODY[] {3}\r\n
                        '''.format(
                            message['from'].encode(),
                            message['to'].encode(),
                            message['subject'].encode(),
                            str(len(message['body'])).encode()
                        ))
                        connection.sendall(message['body'].encode() + b'\r\n')
                        connection.sendall(b')\r\n')
                    else:
                        connection.sendall(b'* NO Message not found\r\n')
                
                elif tokens[0].upper() == 'LOGOUT':
                    break

                else:
                    connection.sendall(b'* BAD Unknown command\r\n')
