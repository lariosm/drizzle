# Baltazar Ortiz
import os
from parser import phoneMessage
from weather_email import sendMessage
from getData import getWeatherData
from tasks.celery import app


api_key = os.getenv('API_KEY')
sender_email = os.getenv('FROM_EMAIL')
receiver_email = os.getenv('SEND_EMAIL')
password = os.getenv('PASSWORD')


@app.task(name="send_email")
def send_email_task():
    data = getWeatherData(api_key)
    premessage = """Subject: Weather Update (Baltazar Ortiz)

    """
    message = phoneMessage(data, premessage)
    print(message)
    sendMessage(message, sender_email, receiver_email, password)
