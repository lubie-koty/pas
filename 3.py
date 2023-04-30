import imaplib

HOST = '212.182.24.27'
PORT = 143
LOGIN = 'pasinf2017@infumcs.edu'
PASSWORD = 'P4SInf2017'

imap = imaplib.IMAP4_SSL(HOST, PORT)
imap.login(LOGIN, PASSWORD)

number_of_messages = 0
status, mailboxes = imap.list()
for mailbox in mailboxes:
    select_status, select_response = imap.select(mailbox.decode('utf-8').split(' "/" ')[1].strip('"'))
    if select_status == 'OK':
        search_status, search_response = imap.search(None, 'ALL')
        messages = search_response[0].split()
        number_of_messages += len(messages)
print(f'{LOGIN} ma {number_of_messages} wiadomosci')

imap.close()
imap.logout()
