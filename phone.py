import smtplib, ssl
import os

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = os.getenv('FROM_EMAIL')  # Enter your address
receiver_email = os.getenv('SEND_EMAIL')  # Enter receiver address
password = os.getenv('PASSWORD')
message = """\
Subject: Weather Update (Baltazar Ortiz)

light rain starting around: 02:00 PM, tomorrow"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    server.quit()