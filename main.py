# Baltazar Ortiz
import os
from parser import phoneMessage
from weather_email import sendMessage
from getData import getWeatherData
from apscheduler.schedulers.blocking import BlockingScheduler

api_key = os.getenv('API_KEY')
sender_email = os.getenv('FROM_EMAIL')
receiver_email = os.getenv('SEND_EMAIL')
password = os.getenv('PASSWORD')

task = BlockingScheduler()


@task.scheduled_job('interval', minutes=3)
def send_email():
    data = getWeatherData(api_key)
    premessage = """Subject: Weather Update (Baltazar Ortiz)

    """
    message = phoneMessage(data, premessage)
    print(message)
    sendMessage(message, sender_email, receiver_email, password)


task.start()
