# Baltazar Ortiz
import os
from parser import phoneMessage
from weather_email import sendMessage
from getData import getWeatherData
from celery import Celery
from celery.schedules import crontab


api_key = os.getenv('API_KEY')
sender_email = os.getenv('FROM_EMAIL')
receiver_email = os.getenv('SEND_EMAIL')
password = os.getenv('PASSWORD')

app = Celery("main",
             broker="redis://localhost",
             backend="redis://localhost")

app.conf.beat_schedule = {
    "trigger-email-notifications": {
        "task": "send_email",
        "schedule": crontab(minute="*")
    }
}


@app.task(name="send_email")
def send_email_task():
    data = getWeatherData(api_key)
    premessage = """Subject: Weather Update (Baltazar Ortiz)

    """
    message = phoneMessage(data, premessage)
    print(message)
    sendMessage(message, sender_email, receiver_email, password)
