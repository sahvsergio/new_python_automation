import config 
from flask import Flask, Response, request 
#from twilio import twiml 
#from twilio import Client 
  
app = Flask(__name__) 
#client = Client(config.TWILIO_ACCOUNT_SID, 
 #                                 config.TWILIO_AUTH_TOKEN) 
  
@app.route('/call', methods=['POST']) 
def outbound_call(): 
    response = twiml.Response() 
    #call = client.calls.create( to=config.MYNUMBER, 
     #           from_=config.CALLERID, 
      #          record='true', 
      #      )
    #return Response(str(response), 200,
     #   mimetype="application/xml") 
    return 'Hello world'
 
if __name__ == '__main__': 
     app.run(debug=True)