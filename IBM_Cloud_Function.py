from flask import Flask, request, jsonify
from twilio.rest import Client
import os

app = Flask(__name__)

# Get credentials from environment
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH = os.environ.get("TWILIO_AUTH")
TWILIO_PHONE = os.environ.get("TWILIO_PHONE")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    date = data.get("date")
    time = data.get("time")
    phone = data.get("phone")  # Must be in international format: +91xxxxxxxxxx

    if not all([date, time, phone]):
        return jsonify({"output": "❗ Missing booking details: date, time, or phone."})

    try:
        client = Client(TWILIO_SID, TWILIO_AUTH)

        message_body = (
            f"✅ Room booked for {date} at {time}.\n"
            f"📞 Contact: {phone}\n"
            f"Thank you for using our chatbot!"
        )

        client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE,
            to=phone
        )

        return jsonify({"output": f"📩 SMS sent to {phone}!"})

    except Exception as e:
        return jsonify({"output": f"❌ Failed to send SMS: {str(e)}"})

@app.route("/")
def index():
    return "📡 SMS Notification Webhook is Running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
