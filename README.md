# 🏒 Oilers Goal Alert System

This is a fully automated Python app that tracks **Edmonton Oilers goals live** using the NHL public API and sends **instant goal alerts via SMS** using Twilio.  
It’s designed to run 24/7 in the cloud and **send real-time notifications directly to your phone** every time the Oilers score.

---

## 📱 Features

- ✅ Real-time goal detection (powered by NHL `score/now` API)
- 📲 SMS alerts to your personal phone via Twilio
- 🔒 Environment variable-based config for secure credential handling
- 🚀 Deployed on [Railway](https://railway.app) to run continuously, even when your computer is off
- ⚙️ Modular, production-ready Python code

---

## 🌐 Live Deployment

This script is deployed on [Railway](https://railway.app), a cloud platform that lets the script run continuously without any servers to manage.

Once deployed:
- It **starts automatically** when Railway boots the container
- You get a **test SMS** confirming it's running
- You’ll receive **live notifications on your phone** the moment the Oilers score during a game

> ⚠️ No need to leave your computer on — alerts are delivered even if you're offline.

---

## 🗂️ Project Structure

```
📦 oilers_goal_alert
├── main.py              # Entry point - runs alert loop
├── goal_checker.py      # NHL score API polling and goal detection
├── sms.py               # Twilio SMS send wrapper
├── config.py            # Loads environment variables
├── utils.py             # Helper functions (optional)
├── requirements.txt     # Dependencies
├── .env.example         # Template for environment variables
└── .gitignore           # Prevents secrets from being pushed
```


## 🚀 Deploying on Railway (Cloud Hosting)

1. **Push this repo to GitHub**
2. Go to [https://railway.app](https://railway.app)
3. Create a **New Project → Deploy from GitHub**
4. Add the required environment variables in Railway’s **Variables tab**
5. Set the start command:
   ```bash
   python main.py
   ```
6. Click **Deploy**

Railway will run your script 24/7 and automatically restart if it crashes.

---

## 💬 Example Alert You’ll Receive

```
🚨 GOAL! McDavid scored for EDM.
Score: EDM 3 - CGY 2
Period 3, Time: 04:12
```

---

## 👤 Designed For

This was built as a personal solution to get **real-time Oilers goal alerts** directly to my phone — no more refreshing NHL.com or missing key moments.

---

## ✅ Future Improvements (Optional)

- Add support for multiple teams
- Build a web UI to let users subscribe to alerts
- Email alerts or Telegram integration
- Web dashboard to display live stats

---


