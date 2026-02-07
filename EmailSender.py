
import smtplib
from email.message import EmailMessage

def codersacademypune_send_mail(sender, app_password, receiver, subject, body):
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(sender, app_password)
    smtp.send_message(msg)
    smtp.quit()

def main():
    sender_email = "codersacademypune@gmail.com"
    app_password = "hvxn usuc pqud allm"
    receiver = "marvellousinfosystem@gmail.com"
    subject = "Test mail from python script"
    body = """Jay Ganesh,

This is a test mail from python script.

Regards,
Aishwarya Dalvi.
"""

    codersacademypune_send_mail(sender_email, app_password, receiver, subject, body)
    print("Mail sent successfully")

if __name__ == "__main__":
    main()