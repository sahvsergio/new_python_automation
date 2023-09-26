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
server.quit


#Email messags with attachments

