
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
    """Respond to incoming requests."""
    if from_number in callers:
	#Greet the caller by name
        greeting = "hi stranger"+ callers[from_number]+" you reach Claire Li.  Just to warn you, something will happen. hahahahaha"
    else:
	greeting = "Hi there. Thanks for calling Claire Li. I'm not available now."
    resp = twilio.twiml.Response()
    resp.say(greeting)
    with resp.gather(numDigits=1, action = "/handle-key",method = "POST") as g:
        g.say("""To speak to real Claire, press 1.
                 Press 2 to record your message.
                 Press any other key to start over.""")
    return str(resp)
@app.route("/handle-key",methods = ['GET','POST'])
def handle_key():
    """Handle key press from a user."""
    #Get the digit pressed by the user
    digit_pressed = request.values.get('Digits',None)
    if digit_pressed =="1":
        resp = twilio.twiml.Response()
        #resp.dial("+13105551212")
        resp.say("It's a trap!")
        resp.play("http://demo.twilio.com/hellomonkey/monkey.mp3")
        return str(resp)
    elif digit_pressed =="2":
        resp = twilio.twiml.Response()
        resp.say("Record your howl after the tone for Claire please.")
        resp.record(maxLength="30",action = "/handle-recording")
        return str(rep)
    else:        
        return redirect("/") 
if __name__ == "__main__":
     port = int(os.environ.get('PORT',5000)) 
     app.run(debug=True,host='0.0.0.0',port=port)
     #app.run(debug=True)

