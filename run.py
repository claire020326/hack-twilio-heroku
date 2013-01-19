
from flask import Flask
import twilio.twiml
import os
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    resp.say("Thanks for calling. You reach Claire Li but she will never pick up your call. Thank you!")
 
    return str(resp)
 
if __name__ == "__main__":
   port = int(os.environ.get('PORT',5000)) 
   app.run(debug=True,host='0.0.0.0',port=port)

