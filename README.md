# AI Room Booking Chatbot

## Demo
![Image](https://github.com/user-attachments/assets/5ef5341f-c848-4c71-be24-7449c0d26e86)



### Instruction

# 🤖 AI Room Booking Chatbot with SMS Notification

This project integrates IBM Watson Assistant with a Flask backend to handle room booking requests and send real-time SMS confirmations using the Twilio API. The chatbot collects booking details from the user, and the Flask app sends a confirmation SMS to the provided phone number.

## 🚀 Features

- Natural language chatbot built using IBM Watson Assistant
- Flask server deployed on Replit
- SMS confirmation sent via Twilio API
- Secure use of environment variables for credentials
- Real-world use case with end-to-end automation

## 🛠 Technologies Used

- IBM Watson Assistant (Dialog-based skill)
- Flask (Python)
- Twilio (SMS API)
- Replit (Cloud hosting for Flask app)

## 🧑‍💻 Setup Instructions

### 1. IBM Watson Assistant Setup

1. Create or log into your IBM Cloud account:  
   https://cloud.ibm.com/

2. Provision Watson Assistant from the catalog:  
   https://cloud.ibm.com/catalog/services/watson-assistant

3. Click “Launch Watson Assistant”

4. Click “Create assistant” → Name it (e.g. `RoomBot`)

5. Click “Add dialog skill” → go to the Upload Skill tab

6. Upload the file: `skill-Room-Booking.json`

### 2. Flask Server on Replit

1. Create a new Replit project or upload `room_booking_sms.py`

2. Install dependencies:
   - `flask`
   - `twilio`

3. Set the following secrets in Replit (under 🔒 "Secrets"):

   | Key           | Value                                 |
   |---------------|----------------------------------------|
   | `TWILIO_SID`   | Your Twilio Account SID               |
   | `TWILIO_AUTH`  | Your Twilio Auth Token                |
   | `TWILIO_PHONE` | Your Twilio phone number (`+1415...`) |

### 3. Twilio Setup

1. Sign up at https://www.twilio.com/try-twilio

2. Get your Account SID, Auth Token, and Twilio Phone Number

3. Go to https://console.twilio.com/us1/develop/phone-numbers/verified  
   ➕ Add the phone number you want to receive SMS (must verify it during trial)

### 4. Connect Watson to Flask Webhook

1. In Watson Assistant, go to:  
   Options > Webhooks > Create Webhook

2. Name it: `main_webhook`  
   URL: `https://your-replit-url.repl.co/webhook`

3. In your dialog node:
   - Add slots: `date`, `time`, `phone`
   - Set webhook to `main_webhook`
   - Payload:
     ```json
     {
       "date": "<?input.date?>",
       "time": "<?input.time?>",
       "phone": "<?input.phone?>"
     }
     ```

## 🧪 Test the Chatbot

Say to your bot:  
“I want to book a room on July 16 at 4 PM. My phone is +91xxxxxxxxxx.”

Watson will collect inputs and trigger your Flask webhook, which sends an SMS using Twilio.

## 📂 Files in this Repository

- `room_booking_sms.py` – Flask backend code
- `skill-Room-Booking.json` – IBM Watson Assistant skill file

## 📌 Credits

Built using IBM Watson Assistant, Flask, Twilio, and Replit  
Developed by [Mohammed Bilal Ulla Shariff]

