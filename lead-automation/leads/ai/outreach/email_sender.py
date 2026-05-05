import smtplib

def send_email(to_email, subject, body):
    sender_email = "your_email@gmail.com"
    password = "your_app_password"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)

    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(sender_email, to_email, message)

    server.quit()

    print(f"Email sent to {to_email}")