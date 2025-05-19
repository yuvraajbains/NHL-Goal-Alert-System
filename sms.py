from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN, TWILIO_PHONE, MY_PHONE
import logging

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_sms(message):
    logging.info(f"📲 Sending SMS: {message}")
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE,
        to=MY_PHONE
    )
