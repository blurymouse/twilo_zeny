from flask import Flask, Response

app = Flask(__name__)

@app.route("/voice")
def voice():
    twiml = """<?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Say voice="women">
            Hello. This is an urgent alert from Zeny.
            New patient data has been sent to you via WhatsApp and email.
            Please check your messages as soon as possible.
        </Say>
    </Response>"""
    return Response(twiml, mimetype='text/xml')