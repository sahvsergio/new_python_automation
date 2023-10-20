"""Sending e-mail messages
E-mail encryption
Beautifying e-mail messages with MIME messages
E-mail messages with attachments
Connecting to your inbox
Fetching and reading e-mail messages
Marking e-mail messages
Clearing up e-mail messages from your inbox
Automating customer support flows with e-mail responses
"""
import smtplib
import config
#sending email
server=smtplib.SMTP('smtp.gmail.com',587)#gmail always run on port 587
server.starttls()
server.login(config.fromaddr,config.password)
msg='Some Nice Msg'
server.sendmail(config.fromaddr,config.toaddr,msg)
server.quit()
#email encription
try:
    server.set_debuglevel(True)
    print('sending ehlo')
    server.ehlo()
    if server.has_extn('STARTTLS'):
        print('starting TLS session')
        server.starttls()
        print('Sending ehlo again')
        server.ehlo
finally:
    server.quit()

#Beautifying e-mail messages with MIME
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.utils

#construct email message with the MIme Module

"""For those who are not aware, a MIME multipart message means both HTML and text content in a single e-mail. 
So, in this code, we create a new multipart MIME message and then add the text content to it."""
fromaddr=config.fromaddr
toaddr=config.toaddr
msg=MIMEMultipart()
msg['Subject']='Hello from the author of this file'
msg['To']=email.utils.formataddr(('Recipient',toaddr))
msg['From']=email.utils.formataddr(('Author',fromaddr))
msgBody=MIMEText(body,'plain')
msg.attach(msgBody)

server=smtplib.SMTPT('smtp.gmail.com',587)
server.starttls()
server.login(fromaddr,config.password)
text=msg.as_string()
print('Text is :',text)
server.sendmail(fromaddr,toaddr,text)
server.quit()


#Email messags with attachments

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import config
fromaddr=config.fromaddr
toaddr=config.toaddr

msg=MIMEMultipart()

msg['From']=config.fromaddr
msg['To']=config.toaddr
msg['Subject']='Email with an attachment'

body='Click to open the attachment'
msg.attach(MIMEText(body,'plain'))

filename='attach.txt'
attachment=open(filename,'rb')

part=MIMEBase('applcation','octect-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment;filename=%s % filename)

msg.attach(part)
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(fromaddr,config.pass)
text=msg.as_string()
server.sendmail(fromaddr,toaddr,text)
server.quit()

#Connecting to your inbox

import config, imaplib

M=imaplib.IMAP4_SSL('imap.gmail.com',993)
M.login(config.fromaddr,config.pass)
print("inbox:")
M.logout()
#selecting inbox
 import config, imaplib
M = imaplib.IMAP4_SSL("imap.gmail.com", 993)
M.login(config.fromaddr, config.password)
print M.list()
M.select('INBOX')
print "Inbox:", M
M.logout()

#Fetching and reading e-mail messages

import config, imaplib
        M = imaplib.IMAP4_SSL("imap.gmail.com", 993) 
        M.login(config.fromaddr, config.password)
        M.select("INBOX")
        
        typ, data = M.search(None, 'SUBJECT', 
    M = imaplib.IMAP4_SSL("imap.gmail.com", 993) 
        M.login(config.fromaddr, config.password)
        M.select("INBOX")
        typ, data = M.search(None, 'SUBJECT', 
                             "Email with an attachment")
        typs, msg = M.fetch(data[0].split()[-1], '(RFC822)')
        print "Message is ", msg[0][1]
        M.close()
        M.logout()
                         "Email with an attachment")
        typs, msg = M.fetch(data[0].split()[-1], '(RFC822)')
        print "Message is ", msg[0][1]
        M.close()
        M.logout()
        
#Marking e-mail messages

import gmail, config
from datetime import date
g = gmail.login(config.fromaddr, config.password)
mails = g.inbox().mail(after=date(2016, 7, 22))
mails[-1].fetch()
print "Email Body:\n", mails[-1].body
g.logout()

#reading unread messages

 import gmail, config
        g = gmail.login(config.fromaddr, config.password)
        mails = g.inbox().mail(unread=True,
        sender='noreply@glassdoor.com')
        mails[-1].fetch()
        mails[-1].read()
        g.logout()
        
#bulk mark them as read and label them
 import gmail, config
        from datetime import date
        g = gmail.login(config.fromaddr, config.password)
        mails = g.inbox().mail(unread=True, 
                               sender='store-news@amazon.in',
                               after=date(2016, 01, 01))
       for email in mails:
           email.read()
           email.add_label("AMAZON")
           g.logout()
#Clearing up e-mail messages from your inbox
   import gmail, config
        g = gmail.login(config.fromaddr, config.password)
        emails = g.inbox().mail(sender='junk@xyz.com')
        if emails:
           for mail in emails:
               mail.delete()
