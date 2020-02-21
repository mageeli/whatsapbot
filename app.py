from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! h"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    phone_no = request.form.get('From')
    # reply = fetch_reply(msg, phone_no)
    # Create reply
    resp = MessagingResponse()
    # resp.message(reply)
    if(msg == '1'):
        resp.message("١- مطار الملك خالد \n ٢- مطار الملك عبدالعزيز")
    else:
        resp.message("شكرا لك على تواصلك مع الروبوت جغرافي. يرجى إخبارنا بما يمكننا القيام به لمساعدتك علما بأني أقدم معلومات عن آراضي التخصصيص في الهيئة العامة للطيران المدني أختر \n١- المطارات الدولية \n٢- المحلية")
        resp.message(phone_no)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)