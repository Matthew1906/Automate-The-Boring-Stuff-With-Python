# SMTP(Simple Mail Transfer Protocol)

import smtplib# simple mail transfer protocol

'''
    Gmail = smtp.gmail.com
    Outlook = smtp-mail.outlook.com
    Yahoo = smtp.mail.yahoo.com
    etc..
'''

connection = smtplib.SMTP("smtp.gmail.com",587)
print(type(connection))
print(connection)
print(connection.ehlo()) # connect to server

connection.starttls()# start encryption first

# allow unsecure third party
# https://myaccount.google.com/lesssecureapps

# connection.login("matthewadrianus@gmail.com",<passwordString>) #pass the email and password
# i'll delete the password for safety

connection.sendmail("matthewadrianus@gmail.com","matthewadrianus@gmail.com","subject: So long...\n\nDear Matthew,\nThis is a test email\n\n")

connection.quit()

# CHECK INBOX -> ill just take notes, because i cant download the library

# IMAP = INTERNET MESSAGE ACCESS PROTOCOL
# COMMUNICATE WITH EMAIL PROVIDER
# complicated protocol

# import imaplib -> dont use this

import imapclient
# import pyzmail36 -> doesnt work in my laptop smh

# conn = imapclient.IMAPClient('imap.gmail.com',ssl=True)
# conn.login(email, password)
# conn.select_folder('INBOX',readonly=True)
# uid = conn.search(['SINCE 12-APR-2021'])

# rawMessage = conn.fetch([uids], ["BODY[]", 'FLAGS'])

# message = pyzmail.PyzMessafe.factory(rawMessage[47474][b'BODY[]'])
# message.get_subject()
# message.get_addresses('from')
# message.get_addresses('to')
# message.get_addresses('bcc)

# message.text_part
# message.html_part

#message.text_part.get_payload().decode('UTF-8')

