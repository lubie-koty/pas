import base64
import telnetlib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

user_email = input('sender email: ')
user_recipients = input('one recipient or multiple recipients (separated by ", ")')
user_subject = input('subject: ')
user_body = input('message: ')

SENDER_EMAIL = 'pas2017@interia.pl'
PASSWORD = 'P4SInf2017'
HOST = 'interia.pl'
PORT = 587

email_message = MIMEMultipart()
email_message['From'] = user_email
email_message['To'] = user_recipients
email_message['Subject'] = user_subject
email_message.attach(MIMEText(user_body, 'html'))

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
    
    split_recipients = user_recipients.split(',')
    if len(split_recipients) > 1:
        for recipient in split_recipients:
            tn.write(b'RCPT TO: <%s>\r\n' % recipient.encode('utf-8'))
            tn.read_until(b'250')
    else:    
        tn.write(b'RCPT TO: <%s>\r\n' % user_recipients.encode('utf-8'))
        tn.read_until(b'250')

    tn.write(b'DATA\r\n')
    tn.read_until(b'354')
    tn.write(b'%s\r\n.\r\n' % email_message.as_bytes())
    tn.read_until(b'250')

    tn.write(b'QUIT\r\n')
    tn.read_until(b'221')
