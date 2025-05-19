# 🏒 Oilers Goal Alert System

A Python app that checks live NHL goal data using the NHL API and sends real-time goal alerts via SMS using Twilio.

## Features
- Live goal detection for selected teams (e.g., Edmonton Oilers)
- SMS alert via Twilio
- Secure environment loading via `.env`
- Modular, production-ready structure

## Setup
1. `pip install -r requirements.txt`
2. Add your `.env` file with Twilio credentials
3. Run: `python main.py`

## Project Structure
📦 oilers_goal_alert
├── main.py
├── sms.py
├── goal_checker.py
├── config.py
├── utils.py
├── requirements.txt
├── .gitignore
└── .env (excluded)

