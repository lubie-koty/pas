import base64
import os
import telnetlib

SENDER_EMAIL = 'pas2017@interia.pl'
PASSWORD = 'P4SInf2017'
HOST = 'interia.pl'
PORT = 587
FILE_PATH = './tekst.txt'

user_email = input('sender email: ')
user_recipients = input('one recipient or multiple recipients (separated by ", ")')
user_subject = input('subject: ')
user_body = input('message: ')

email_kwargs = {
    'from': user_email,
    'to': user_recipients,
    'subject': user_subject,
    'body': user_body,
    'file_name': os.path.basename(FILE_PATH)
}

with open(FILE_PATH, 'r') as f:
    email_kwargs['file_content'] = base64.b64encode(f.read())

email_message = '''
Content-Type: multipart/mixed; boundary="===============2445749806980231662=="
MIME-Version: 1.0
From: {from}
To: {to}
Subject: {subject}

--===============2445749806980231662==
Content-Type: text/plain; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit

{body}

--===============2445749806980231662==
Content-Type: application/txt
MIME-Version: 1.0
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename="{file_name}"

{file_content}

--===============2445749806980231662==--

'''.format(**email_kwargs)

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
    tn.write(b'%s\r\n.\r\n' % email_message.encode('utf-8'))
    tn.read_until(b'250')

    tn.write(b'QUIT\r\n')
    tn.read_until(b'221')
