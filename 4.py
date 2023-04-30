import email
import imaplib

HOST = '212.182.24.27'
PORT = 143
LOGIN = 'pasinf2017@infumcs.edu'
PASSWORD = 'P4SInf2017'

imap = imaplib.IMAP4_SSL(HOST, PORT)
imap.login(LOGIN, PASSWORD)
imap.select()

status, response = imap.search(None, 'UNSEEN')
if status != 'OK':
    print('Skrzynka nie zawiera nieprzeczytanych wiadomosci')
else:
    messages = response[0].split()
    for message in messages:
        message_status, message_response = imap.fetch(message, '(RFC822)')
        if message_status == 'OK':
            email_message = email.message_from_bytes(message_response[0][1])
            print('From:', email_message['From'])
            print('To:', email_message['To'])
            print('Subject:', email_message['Subject'])
            print('Date:', email_message['Date'])
            print('Body:', email_message.get_payload())
            print('\n')
            imap.store(message, '+FLAGS', '\\Seen')

imap.close()
imap.logout()
