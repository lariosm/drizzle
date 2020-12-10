from datetime import datetime, timedelta

def is_raining(value):
    return value >= 500 and value < 600

def getMidnight():
    tomorrow = datetime.now() + timedelta(days=1)
    return tomorrow.replace(hour=0, minute=0, second=0, microsecond=0)
    
def getTomorrowForecast(data):
    return data["daily"][1]["weather"][0]

def getTomorrowAt(data, hour):
    return data["hourly"][hour]["weather"][0]["id"]

def phoneMessage(data, message):
    weather_tomorrow = getTomorrowForecast(data)

    if is_raining(weather_tomorrow["id"]):
        startRainTime = 0
        for i in range(int(len(data["hourly"]) / 2)):
            current_hour_weather = getTomorrowAt(data,i)
            if is_raining(current_hour_weather):
                currentTime = data["hourly"][i]["dt"]
                startRainTime = datetime.fromtimestamp(currentTime)
                break
        time_of_day = startRainTime.strftime("%I:%M %p")
        midnight = getMidnight()
        when = "tomorrow" if startRainTime > midnight else "tonight"
        message = message + weather_tomorrow["description"] + \
        " starting around: " + time_of_day + ", " + when
    else:
        message = message + "it will not rain tomorrow"

    return message
