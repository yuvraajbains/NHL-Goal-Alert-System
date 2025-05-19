import time
from sms import send_sms
from goal_checker import check_for_goals
from utils import setup_logging, setup_graceful_shutdown

def main():
    setup_logging()
    setup_graceful_shutdown()

    print("🏒 NHL Goal Alert: Edmonton Oilers")
    send_sms("🚨 TEST: Oilers goal alert system is now running.")

    while True:
        check_for_goals()
        time.sleep(30)

if __name__ == "__main__":
    main()
