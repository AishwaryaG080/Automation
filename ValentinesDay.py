import smtplib
from email.message import EmailMessage
import time
from datetime import datetime

# ---------- EMAIL FUNCTION ----------
def send_mail(sender, app_password, receiver, subject, body):
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(sender, app_password)
    smtp.send_message(msg)
    smtp.quit()

# ---------- VALENTINE SERIES ----------
messages = [
    ("Midnight Valentine ❤️",
     "It’s 12 AM… Happy Valentine’s Day, my love.\n\n"
     "Every day with you feels like home.\n"
     "you are my safe place, my forever.\n\n"
     "I Love You Aho❤️"
     "– Aishwarya 💖"),

    ("Still thinking of you 🌙",
     "Even at 2 AM, my heart finds its way to you.\n"
     "Some connections don’t sleep.\n\n"
     "Always,\nAishwarya ❤️"),

    ("Early morning thoughts ☀️",
     "Good morning (almost 😄).\n"
     "I hope today starts with a smile.\n\n"
     "Love,\nAishwarya 💕"),

    ("Good Morning Valentine 🌹",
     "Wake up knowing that someone truly cares about you.\n\n"
     "That someone is me.\n\n"
     "– Aishwarya"),

    ("A little reminder 💌",
     "In case the day gets busy —\n"
     "you are important.\n"
     "you are appreciated.\n\n"
     "❤️ Aishwarya"),

    ("Mid-morning smile 😊",
     "If this email made you smile,\n"
     "then my day is already better.\n\n"
     "– Aishwarya"),

    ("Happy Valentine’s Day ❤️",
     "Half the day is gone, but my feelings remain constant.\n\n"
     "Thank you for being you.\n\n"
     "With love,\nAishwarya 💖"),

    ("Thinking of you 💭",
     "No matter how busy life gets,\n"
     "you always cross my mind.\n\n"
     "Forever,\nAishwarya"),

    ("Almost evening 🌆",
     "As the sun slowly sets,\n"
     "I just want you to know how much I value you.\n\n"
     "💞 Aishwarya"),

    ("Evening warmth 🕯️",
     "Some people bring warmth just by existing.\n\n"
     "You are one of them.\n\n"
     "– Aishwarya"),

    ("One more before night 🌙",
     "Today felt special because you were part of it.\n\n"
     "Thank you for being my Valentine.\n\n"
     "❤️ Aishwarya"),

    ("Last one… for now 💘",
     "Before the day ends,\n"
     "I want you to know you are my favorite thought.\n\n"
     "Happy Valentine’s Day Aho❤️"
     "I Love You Aho❤️"
     "Good night,\nAishwarya 🌹")
]

# ---------- FINAL REVEAL ----------
final_reveal_subject = "This was never just emails ❤️"

final_reveal_body = """All day long, these emails appeared quietly in your inbox.

But behind every message was intention.
Thought.
Feeling.

I didn’t do this because it was Valentine’s Day.
I did this because of *you*.

Because you matter to me.
Because you cross my mind more often than you realize.
Because I wanted you to feel—at least once today—how special you truly are.

So here it is, honestly and without hiding:

❤️ I care about you.
❤️ I wanted this day to feel different for you.
❤️ And yes… I wanted to be the reason you smiled today.

If these messages made your day even a little warmer,
then every line of code was worth it.

Happy Valentine’s Day Aho❤️
I Love You Aho❤️

— Aishwarya
"""

# ---------- MAIN ----------
def main():
    sender_email = "aishwaryagaikwad080@gmail.com"
    app_password = "hvxn usuc pqud allm"
    receiver = "guruprasad.dalvi7@gmail.com"

    print("💌 Valentine script started at", datetime.now())

    # Send messages every 2 hours
    for subject, body in messages:
        send_mail(sender_email, app_password, receiver, subject, body)
        print("Sent:", subject)
        time.sleep(2 * 60 * 60)  # 2 hours

    # Final reveal at the end
    send_mail(sender_email, app_password, receiver,
              final_reveal_subject, final_reveal_body)
    print("💖 Final reveal sent!")

if __name__ == "__main__":
    main()