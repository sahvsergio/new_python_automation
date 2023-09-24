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
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(config.fromaddr,config.password)
msg='Some Nice Msg'
server.sendmail(config.fromaddr,config.toaddr,msg)
server.quit()