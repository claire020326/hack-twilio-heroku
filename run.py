from flask import Flask,request,redirect
import twilio.twiml
import os
 
app = Flask(__name__)
callers = {
"+1510542624X":"Chase",
"+1714267039X":"Siyao",
"+1510517802X":"Lisa",
"+1515509442X":"Shirly",
"+1615429731X":"Cynthia",
"+15072029530":"Claire Li",
} 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    from_number = request.values.get('From',None)
    """Respond to incoming requests."""
    if from_number in callers:
	#Greet the caller by name
        greeting = "hi stranger! I know you are "+ callers[from_number]+". Just so you know you reach Claire Li. Watch out! something will happen.`"
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
        resp.say("It's a trap!")
        resp.play("http://demo.twilio.com/hellomonkey/monkey.mp3")
        return str(resp)
    
    elif digit_pressed =="2":
        resp = twilio.twiml.Response()
        resp.say("Record your howl after the tone for Claire please.")
        resp.record(maxLength="30",action = "/handle-recording")
        return str(resp)
    else:        
        return redirect("/") 
@app.route("/handle-recording", methods=['GET', 'POST'])
def handle_recording():
    """Play back the caller's recording."""
 
    recording_url = request.values.get("RecordingUrl", None)
 
    resp = twilio.twiml.Response()
    resp.say("Thanks for howling... take a listen to what you howled.")
    resp.play(recording_url)
    resp.say("Goodbye.")
    return str(resp)
#@app.route("/handle-recording",methods = ['GET','POST'])
#def handle_recording():
#    """Play the caller's recording."""
#    recording_url = request.values.get("RecordingUrl",None)
#    resp = twilio.twiml.Response()
#    resp.say("Thanks for howling...listen to your howl before Claire suffer from it.")
#    resp.play(recording_url)
#    resp.say("Good..Bye")
#    return str(resp)
if __name__ == "__main__":
     port = int(os.environ.get('PORT',5000)) 
     app.run(debug=True,host='0.0.0.0',port=port)
     #app.run(debug=True)

