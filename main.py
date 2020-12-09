# Baltazar Ortiz
import os
from datetime import datetime, timedelta
import requests
import json

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
    print(f'{weather_tomorrow["description"]} starting around: {time_of_day}, {when}')
else:
    print("it will not rain tomorrow")
