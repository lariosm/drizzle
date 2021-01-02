# Baltazar Ortiz
import os
from parser import phoneMessage
from weather_email import sendMessage
from getData import getWeatherData
from apscheduler.schedulers.blocking import BlockingScheduler
from pytz import utc

api_key = os.getenv('API_KEY')
sender_email = os.getenv('FROM_EMAIL')
receiver_email = os.getenv('SEND_EMAIL')
password = os.getenv('PASSWORD')

task = BlockingScheduler(timezone=utc)


# Sends out an email every day at 17:30 (9:30 AM Pacific time)
@task.scheduled_job('cron', hour=17, minute=30)
def send_email():
    data = getWeatherData(api_key)
    premessage = """Subject: Weather Update (Baltazar Ortiz)

    """
    message = phoneMessage(data, premessage)
    sendMessage(message, sender_email, receiver_email, password)


task.start()
