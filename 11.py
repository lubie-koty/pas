import email
import os
import telnetlib

HOST = 'interia.pl'
PORT = 110
LOGIN = 'pas2017@interia.pl'
PASSWORD = 'P4SInf2017'

message_num = input('message number: ')

with telnetlib.Telnet(HOST, PORT) as tn:
    print(tn.read_until(b'\n'))
    tn.write(b'user %s\n' % LOGIN.encode('ascii'))
    tn.write(b'pass %s\n' % PASSWORD.encode('ascii'))
    
    response = tn.read_until(b'\n').decode('ascii')
    if response.startswith('+OK'):
        tn.write(b'retr %s\n' % message_num.encode('ascii'))
        retr_response = tn.read_until('.\n').decode('ascii')
        
        for email_part in email.message_from_string(retr_response).walk():
            if email_part.get_content_maintype() == 'multipart':
                continue
            if email_part.get_content_disposition() is None:
                continue
            
            file_name = email_part.get_filename()
            if file_name is None:
                continue
            
            file_path = os.path.join(os.getcwd(), file_name)
            with open(file_path, 'wb') as f:
                f.write(email_part.get_payload(decode=True))

        print(f'image from message {message_num} was saved to:\n{file_path}')

    else:
        print(f'Login failed: {response}')

    tn.write(b'quit\n')
    print(tn.read_all().decode('ascii'))
