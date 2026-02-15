import sys
import time
import logging

from modules.logger import create_log_file
from modules.process_monitor import (
    monitor_threads,
    monitor_open_files,
    monitor_memory,
    get_summary
)
from modules.mailer import send_email


def validate_args():
    if len(sys.argv) != 4:
        print("Usage: PlatformSurveillance.py <LogDir> <Email> <IntervalMin>")
        sys.exit()

    log_dir = sys.argv[1]
    receiver = sys.argv[2]

    try:
        interval = int(sys.argv[3]) * 60
    except ValueError:
        print("Interval must be integer minutes")
        sys.exit()

    return log_dir, receiver, interval


def main():
    log_dir, receiver, interval = validate_args()
    log_path = create_log_file(log_dir)

    logging.info("Platform Surveillance Started")

    while True:
        try:
            monitor_threads()
            monitor_open_files()
            monitor_memory()

            summary = get_summary()
            send_email(receiver, log_path, summary)

            time.sleep(interval)

        except KeyboardInterrupt:
            logging.info("Program terminated by user")
            break
        except Exception as e:
            logging.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()