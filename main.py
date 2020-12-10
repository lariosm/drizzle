# Baltazar Ortiz
import os
import requests
import json
import smtplib, ssl
from parser import phoneMessage

url = "https://api.openweathermap.org/data/2.5/onecall"
url = url + "?lat=44.950433005684886&lon=-122.99038677842634"
url = url + "&exclude=current,minutely&appid="
url = url + os.getenv('API_KEY')
url = url + "&units=imperial"

r = requests.get(url)
data = json.loads(r.text)

premessage = """Subject: Weather Update (Baltazar Ortiz)

"""
message = phoneMessage(data, premessage)

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = os.getenv('FROM_EMAIL')  # Enter your address
receiver_email = os.getenv('SEND_EMAIL')  # Enter receiver address
password = os.getenv('PASSWORD')

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    server.quit()
