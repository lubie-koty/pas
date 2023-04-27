import base64
import os
import telnetlib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

SENDER_EMAIL = 'pas2017@interia.pl'
RECEIVER_EMAIL = 'pasinf2017@interia.pl'
PASSWORD = 'P4SInf2017'
HOST = 'interia.pl'
PORT = 587
FILE_PATH = './moj_kot_misio.jpg'

EMAIL_SUBJECT = 'Fajny mail'
EMAIL_BODY = '''
Hej,
programowanie aplikacji sieciowych jest super.

Pozdrawiam,
Kolega
'''

email_message = MIMEMultipart()
email_message['From'] = SENDER_EMAIL
email_message['To'] = RECEIVER_EMAIL
email_message['Subject'] = EMAIL_SUBJECT
email_message.attach(MIMEText(EMAIL_BODY, 'plain'))
with open(FILE_PATH, 'rb') as f:
    image_file = MIMEImage(f.read())
    image_file.add_header('Content-Disposition', 'attachment', filename=os.path.basename(FILE_PATH))
    email_message.attach(image_file)


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

    tn.write(b'MAIL FROM: <%s>\r\n' % SENDER_EMAIL.encode('utf-8'))
    tn.read_until(b'250')
    tn.write(b'RCPT TO: <%s>\r\n' % RECEIVER_EMAIL.encode('utf-8'))
    tn.read_until(b'250')
    tn.write(b'DATA\r\n')
    tn.read_until(b'354')
    tn.write(b'%s\r\n.\r\n' % email_message.as_bytes())
    tn.read_until(b'250')

    tn.write(b'QUIT\r\n')
    tn.read_until(b'221')
