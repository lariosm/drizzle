from datetime import datetime, timedelta


def is_raining(value):
    return value >= 500 and value < 600


def get_midnight():
    tomorrow = datetime.now() + timedelta(days=1)
    return tomorrow.replace(hour=0, minute=0, second=0, microsecond=0)


def get_tomorrows_forecast(data):
    return data["daily"][1]["weather"][0]


def get_tomorrow_at(data, hour):
    return data["hourly"][hour]["weather"][0]["id"]


def get_hourly_at(data, hour):
    return data["hourly"][hour]["dt"]


def phone_message(data, message):
    weather_tomorrow = get_tomorrows_forecast(data)

    if is_raining(weather_tomorrow["id"]):
        start_rain_time = 0

        for i in range(int(len(data["hourly"]) / 2)):
            current_hour_weather = get_tomorrow_at(data, i)

            if is_raining(current_hour_weather):
                current_time = get_hourly_at(data, i)
                start_rain_time = datetime.fromtimestamp(current_time)
                break

        time_of_day = start_rain_time.strftime("%I:%M %p")
        midnight = get_midnight()
        when = "tomorrow" if start_rain_time > midnight else "tonight"
        message = message + weather_tomorrow["description"] + \
            " starting around: " + time_of_day + ", " + when
    else:
        message = message + "it will not rain tomorrow"

    return message
