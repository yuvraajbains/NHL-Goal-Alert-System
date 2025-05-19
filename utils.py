import logging
import signal
import sys

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s — %(levelname)s — %(message)s"
    )

def setup_graceful_shutdown():
    def handle_exit(sig, frame):
        print("\n🛑 Stopping script...")
        sys.exit(0)

    signal.signal(signal.SIGINT, handle_exit)
    signal.signal(signal.SIGTERM, handle_exit)
