
from flask import Flask,request,redirect
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
        caller = callers[from_number]
    else:
	caller = "Monkey"
    resp = twilio.twiml.Response()
    resp.say("Hi "+caller+" this is Claire Li's private number")
    resp.play("http://demo.twilio.com/hellomonkey/monkey.mp3")
    with resp.gather(numDigits=1, action = "/handle-key",method = "POST") as g:
        g.say("To speak to real Claire, press 1. Press any other key to start over.")
    return str(resp)
#@app.route("/handle-key",methods = ['GET','POST'])
#def handle_key():
#    """Handle key press from a user."""
#    #Get the digit pressed by the user
#    digit_pressed = request.values.get('Digits',None)
#    if digit_pressed =="1":
#        resp = twiml.Response()
#        #resp.dial("+13105551212")
#        resp.say("It's a trap, haha!")
#        resp.play("http://demo.twilio.com/hellomonkey/monkey.mp3")
#        return str(resp)
#    else:
#        return redirect("/") 
@app.route("/handle-key", methods=['GET', 'POST'])
def handle_key():
    """Handle key press from a user."""
 
    # Get the digit pressed by the user
    digit_pressed = request.values.get('Digits', None)
    if digit_pressed == "1":
        resp = twiml.Response()
        # Dial (310) 555-1212 - connect that number to the incoming caller.
        resp.dial("+13105551212")
        # If the dial fails:
        resp.say("The call failed, or the remote party hung up. Goodbye.")
 
        return str(resp)
 
    # If the caller pressed anything but 1, redirect them to the homepage.
    else:
        return redirect("/")
if __name__ == "__main__":
     port = int(os.environ.get('PORT',5000)) 
     app.run(debug=True,host='0.0.0.0',port=port)
     #app.run(debug=True)

