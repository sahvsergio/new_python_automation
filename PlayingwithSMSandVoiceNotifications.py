"""
Chapter 4. Playing with SMS and Voice Notifications
Cloud telephony is the technology that moves your phone system to the cloud. This has made sure that we can now explore the possibilities of automation with SMS and voice notifications. This chapter begins with an introduction to cloud telephony and covers automation of business use cases with text and voice messages in Python.

In this chapter, we will cover the following recipes:

Registering with a cloud telephony provider
Sending text messages
Receiving SMS messages
SMS workflows for Domino's
Sending voice messages
Receiving voice calls
Building your own customer service software"""


#sending text message
import config
from flask import Flask
from twilio.rest import Client

app=Flask(__name__)
#client = Client(config.TWILIO_ACCOUNT_SID,config.TWILIO_AUTH_TOKEN)

#message=client.messages.create(to=config.MYNUMBER,
 #                              from_= config.CALLERID,body='Hey, this is cool!x')


#receiving sms messages
from flask import Flask
app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def respond_sms():
    resp = twilio.twiml.Response()
    resp.message("Thanks for your query. We will get back to you soon")
    #return str(resp)
    return 'Hello World'
        
        
if __name__ == "__main__":
    app.run(debug=True,host='127.0.0.1')

