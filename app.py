from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()
    if(msg == '1'):
        resp.message("١- مطار الملك خالد \n ٢- مطار الملك عبدالعزيز")
    else:
        resp.message("شكرا لك على تواصلك مع الروبوت جغرافي. يرجى إخبارنا بما يمكننا القيام به لمساعدتك علما بأني أقدم معلومات عن آراضي التخصصيص في الهيئة العامة للطيران المدني أختر \n١- المطارات الدولية \n٢- المحلية")


    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)