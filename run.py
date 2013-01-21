
from flask import Flask
import twilio.twiml
import os
 
app = Flask(__name__)
callers = {
"+17142670397":"Siyao","+15105178020":"Lisa Li","+15155094420":"Shirly Chen","+16154297319":"Cynthia Feng","+15072029530":"Claire Li",
} 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    from_number = request.values.get('From',None)
    #"""Respond to incoming requests."""
    if from_number in callers:
	#Greet the caller by name
	resp.say("Hello Hello" + callers[from_number])
    else:
	resp.say("Hi there!")
    #resp = twilio.twiml.Response()
    #resp.say("Thanks for calling. You reach Claire Li but she is not available now and she knows you are Junchao Lu. Don't expect her to take your call!")
    with resp.gather(numDigits=1, action = "/handle-key",method = "POST") as g:
        g.say("To speak to real Claire, press 1. Press any other key to start over.")
    return str(resp)
@app.route("/handle-key",methods = ['GET','POST'])
def handle_key():
  #Get the digit pressed by the user
  digit_pressed = request.values.get('Digits',None)
  if digit_pressed =="1":
    resp = twiml.Responsee()
    resp.dial("+13105551212")
    resp.say("The call failed. It's a trap, haha!")
    return str(resp)
  else:
       return redirect("/") 
if __name__ == "__main__":
   port = int(os.environ.get('PORT',5000)) 
   app.run(debug=True,host='0.0.0.0',port=port)

