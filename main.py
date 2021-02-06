# Baltazar Ortiz
import os
from parser import phone_message
from weather_email import send_message
from getData import get_weather_data
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
    data = get_weather_data(api_key)
    premessage = """Subject: Weather Update (Baltazar Ortiz)

    """
    message = phone_message(data, premessage)
    send_message(message, sender_email, receiver_email, password)


task.start()
