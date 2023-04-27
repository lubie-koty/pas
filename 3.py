import base64
import telnetlib

SENDER_EMAIL = 'pas2017@interia.pl'
RECEIVER_EMAIL = 'pasinf2017@interia.pl'
PASSWORD = 'P4SInf2017'
HOST = 'interia.pl'
PORT = 587

email_subject = 'Fajny mail'
email_body = '''
Hej,
programowanie aplikacji sieciowych jest super.

Pozdrawiam,
Kolega
'''

with telnetlib.Telnet(HOST, PORT) as tn:
    tn.read_until(b'220')

    tn.write(b'EHLO itsme\r\n')
    tn.read_until(b'250')

    tn.write(b'STARTTLS\r\n')
    tn.read_until(b'220')

    tn.write(b'AUTH LOGIN\r\n')
    tn.read_until(b'334')
    tn.write(base64.b64encode(SENDER_EMAIL.encode('utf-8')) + b'\r\n')
    tn.read_until(b'334')
    tn.write(base64.b64encode(PASSWORD.encode('utf-8')) + b'\r\n')
    tn.read_until(b'235')

    tn.write(b'MAIL FROM: <%s>\r\n' % 'art.zelazko@gmail.com'.encode('utf-8'))
    tn.read_until(b'250')
    tn.write(b'RCPT TO: <%s>\r\n' % RECEIVER_EMAIL.encode('utf-8'))
    tn.read_until(b'250')
    tn.write(b'DATA\r\n')
    tn.read_until(b'354')
    tn.write(b'Subject: %s\r\n\r\n%s\r\n.\r\n' % (email_subject.encode('utf-8'), email_body.encode('utf-8')))
    tn.read_until(b'250')

    tn.write(b'QUIT\r\n')
    tn.read_until(b'221')
