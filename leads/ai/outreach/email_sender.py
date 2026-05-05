import smtplib
import os

def send_email(to_email, subject, body):
    sender_email = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")

    if not sender_email or not password:
        print("EMAIL_USER or EMAIL_PASS not set. Skipping email send.")
        return

    # For Office 365 (albany.edu likely uses this)
    server = smtplib.SMTP("smtp.office365.com", 587)
    server.starttls()
    server.login(sender_email, password)

    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(sender_email, to_email, message)

    server.quit()

    print(f"Email sent to {to_email}")