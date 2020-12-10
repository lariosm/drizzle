# Baltazar Ortiz
import os
from datetime import datetime, timedelta
import requests
import json
import smtplib, ssl

def is_raining(value):
    return value >= 500 and value < 600

url = "https://api.openweathermap.org/data/2.5/onecall"
url = url + "?lat=44.950433005684886&lon=-122.99038677842634"
url = url + "&exclude=current,minutely&appid="
url = url + os.getenv('API_KEY')
url = url + "&units=imperial"

r = requests.get(url)
data = json.loads(r.text)

next_day = data["daily"][1]
weather_tomorrow = next_day["weather"][0]
startRainTime = 0
message = """Subject: Weather Update (Baltazar Ortiz)

"""
if is_raining(weather_tomorrow["id"]):
    for i in range(int(len(data["hourly"]) / 2)):
        current_hour_weather = data["hourly"][i]["weather"][0]["id"]
        if is_raining(current_hour_weather):
            currentTime = data["hourly"][i]["dt"]
            startRainTime = datetime.fromtimestamp(currentTime)
            break
    time_of_day = startRainTime.strftime("%I:%M %p")
    tomorrow = datetime.now() + timedelta(days=1)
    midnight = tomorrow.replace(hour=0, minute=0, second=0, microsecond=0)
    when = ""
    if startRainTime > midnight:
        when = "tomorrow"
    else:
        when = "tonight"
    message = message + weather_tomorrow["description"] + " starting around: " + time_of_day + ", " + when
else:
    message = message + "it will not rain tomorrow"

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
