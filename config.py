import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
MY_PHONE = os.getenv("MY_PHONE")
WATCH_TEAMS = ["Oilers", "Leafs"]  # Can expand to be dynamic if needed

required = [ACCOUNT_SID, AUTH_TOKEN, TWILIO_PHONE, MY_PHONE]
if not all(required):
    raise EnvironmentError("Missing one or more environment variables in .env")
