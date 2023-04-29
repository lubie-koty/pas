import telnetlib

HOST = 'interia.pl'
PORT = 110
LOGIN = 'pas2017@interia.pl'
PASSWORD = 'P4SInf2017'

with telnetlib.Telnet(HOST, PORT) as tn:
    print(tn.read_until(b'\n'))
    tn.write(b'user %s\n' % LOGIN.encode('ascii'))
    tn.write(b'pass %s\n' % PASSWORD.encode('ascii'))
    
    response = tn.read_until(b'\n').decode('ascii')
    if response.startswith('+OK'):
        tn.write(b'list\n')
        list_response = tn.read_until(b'.\n')
        messages = list_response.decode('ascii').split('\n')[1:-2]

        first_message = messages[0].split()
        min_size_message = first_message[0]
        min_size = int(first_message[1])

        for message in messages[1:]:
            message_info = message.split()
            if int(message_info[1]) < min_size:
                min_size_message = message_info[0]

        tn.write(b'dele %s\n' % min_size_message.encode('ascii'))
        print(tn.read_until('.\n').decode('ascii'))
    else:
        print(f'Login failed: {response}')

    tn.write(b'quit\n')
    print(tn.read_all().decode('ascii'))
