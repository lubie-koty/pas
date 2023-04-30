import telnetlib
import base64

HOST = '212.182.24.27'
PORT = 143
LOGIN = 'pasinf2017@infumcs.edu'
PASSWORD = 'P4SInf2017'

command_number = 1

with telnetlib.Telnet(HOST, PORT) as tn:
    tn.read_until(b'OK')

    tn.write(b'%s LOGIN %s %s\r\n' % (command_number, LOGIN, PASSWORD))
    response = tn.read_until(b'%s OK' % command_number)
    command_number += 1

    tn.write(b'%s LIST "" *\r\n' % command_number)
    response = tn.read_until(b'%s OK' % command_number)
    command_number += 1

    mailboxes = response.split(b'\r\n')[:-2]
    for mailbox in mailboxes:
        parts = mailbox.split(b'"')
        name = parts[-2].decode('utf-8')
        tn.write(b'%s SELECT %s\r\n' % (command_number, name))
        response = tn.read_until(b'%s OK' % command_number)
        command_number += 1

        tn.write(b'%s STATUS %s (MESSAGES)\r\n' % (command_number, name))
        response = tn.read_until(b'%s OK' % command_number)
        command_number += 1
        num_messages = int(response.split(b'MESSAGES ')[1].split(b')')[0])
        print(f'{name}: {num_messages} messages')

        if num_messages > 0:
            tn.write(b'%s FETCH 1 (BODY.PEEK[TEXT])\r\n' % command_number)
            response = tn.read_until(b'%s OK' % command_number)
            command_number += 1
            message_content = response.split(b'{')[1].split(b'}\r\n')[0]
            decoded_content = base64.b64decode(message_content).decode('utf-8')
            print(f'mailbox {name} first message:\n{decoded_content}')

            tn.write(b'%s STORE 1 +FLAGS (\\Seen)\r\n' % command_number)
            response = tn.read_until(b'%s OK' % command_number)
            command_number += 1

    tn.write(b'%s LOGOUT\r\n' % command_number)
