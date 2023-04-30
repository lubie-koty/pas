import imaplib
import sys

HOST = '212.182.24.27'
PORT = 143
LOGIN = 'pasinf2017@infumcs.edu'
PASSWORD = 'P4SInf2017'
MAILBOX = 'Inbox'

imap = imaplib.IMAP4_SSL(HOST, PORT)
imap.login(LOGIN, PASSWORD)
imap.select(MAILBOX)

if len(sys.argv) > 1:
    message_to_be_deleted = sys.argv[1]
else:
    status, response = imap.search(None, 'ALL')
    message_to_be_deleted = response[0].split()[0]

imap.store(message_to_be_deleted, '+FLAGS', '\\Deleted')
imap.expunge()

imap.close()
imap.logout()
