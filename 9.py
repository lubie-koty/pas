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

        max_size = 0
        max_size_message = None
        for message in list_response.decode('ascii').split('\n')[1:-2]:
            message_info = message.split()
            if int(message_info[1]) > max_size:
                max_size_message = message_info[0]

        tn.write(b'retr %s\n' % max_size_message.encode('ascii'))
        retr_response = tn.read_until('.\n').decode('ascii')
        print(f'biggest size message:\n{retr_response}')
    else:
        print(f'Login failed: {response}')

    tn.write(b'quit\n')
    print(tn.read_all().decode('ascii'))
