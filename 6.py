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
        tn.write(b'stat\n')
        stat_response = tn.read_until(b'\n')
        status = stat_response.decode('ascii').split()
        number_of_messages = int(status[1])
        print(f'Number of messages: {number_of_messages}')
    else:
        print(f'Login failed: {response}')

    tn.write(b'quit\n')
    print(tn.read_all().decode('ascii'))
