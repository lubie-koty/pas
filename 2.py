import imaplib

HOST = '212.182.24.27'
PORT = 143
LOGIN = 'pasinf2017@infumcs.edu'
PASSWORD = 'P4SInf2017'
MAILBOX = 'Inbox'

imap = imaplib.IMAP4_SSL(HOST, PORT)
imap.login(LOGIN, PASSWORD)
imap.select(MAILBOX)

status, response = imap.search(None, 'ALL')
messages = response[0].split()
print(f'Skrzynka {MAILBOX} zawiera {len(messages)} wiadomosci')

imap.close()
imap.logout()
