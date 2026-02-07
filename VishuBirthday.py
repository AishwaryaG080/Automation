import smtplib
from email.message import EmailMessage
import time
from datetime import datetime

def send_mail(sender, app_password, receiver, subject, body):
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, app_password)
        smtp.send_message(msg)

# -------- BIRTHDAY MESSAGES --------
birthday_messages = [
    (
        "Happy Birthday 🎉🎂",
        """

A gadva, Happy Birthday!!

— Aishwarya
"""
    ),
    (
        "Just a reminder 😊",
        """Hey, Happy Birthday,

Gadva, kasa vatla maza surprise....hahahahaha

— Aishwarya
"""
    ),
    (
        """
Happy Birthday once again ❤️
— Aishwarya
"""
    )
]

def main():
    sender_email = "codersacademypune@gmail.com"
    app_password = "hvxn usuc pqud allm"
    receiver_email = "aishwaryagaikwad080@gmail.com"

    print("🎂 Birthday script started at", datetime.now())

    # 12:00 AM message
    subject, body = birthday_messages[0]
    send_mail(sender_email, app_password, receiver_email, subject, body)
    print("Sent midnight birthday wish 🎉")

    # Wait till 10 AM (10 hours)
    time.sleep(10 * 60 * 60)

    subject, body = birthday_messages[1]
    send_mail(sender_email, app_password, receiver_email, subject, body)
    print("Sent morning message 😊")

    # Wait till 8 PM (10 more hours)
    time.sleep(10 * 60 * 60)

    subject, body = birthday_messages[2]
    send_mail(sender_email, app_password, receiver_email, subject, body)
    print("Sent final birthday message ❤️")

if __name__ == "__main__":
    main()