import smtplib
from email.message import EmailMessage

def send_email(sender, password, receiver, log_file, zip_file):
    msg = EmailMessage()
    msg["Subject"] = "Backup Completed"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("Backup completed successfully.")

    for file in [log_file, zip_file]:
        with open(file, "rb") as f:
            msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=file)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)