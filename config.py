#a configuration file for the twilio and playing with SMS and voice telephony
import os

TWILIO_ACCOUNT_SID = 'Account SID' 
TWILIO_AUTH_TOKEN = 'Auth Token' 
CALLERID = '+Rented Number' 
MYNUMBER = '+Your Number' 

fromaddr =os.environ.get('inbound_email')
password=os.environ.get('gpass')
toaddr=os.environ.get('outbound_email')