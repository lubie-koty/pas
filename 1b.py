import smtplib
from email.mime.text import MIMEText

EMAIL = 'pas2017@interia.pl'
PASSWORD = 'P4SInf2017'
HOST = 'interia.pl'
PORT = 465


def send_email(sender_email, recipient_email, subject, message):
    email_message = MIMEText(message)
    email_message['Subject'] = subject
    email_message['From'] = sender_email
    email_message['To'] = recipient_email

    server = smtplib.SMTP_SSL(HOST, PORT)
    server.starttls()
    server.login(EMAIL, PASSWORD)

    server.sendmail(sender_email, recipient_email, email_message.as_string())
    print("Email has been sent!")

    server.quit()


if __name__ == '__main__':
    sender = input('sender: ')
    recipient = input('recipient: ')
    subject = input('subject: ')
    message = input('message: ')
    send_email(sender, recipient, subject, message)
