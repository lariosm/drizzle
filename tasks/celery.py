import os
from celery import Celery
from celery.schedules import crontab

app = Celery("tasks",
             broker=os.getenv("BROKER_URL"),
             backend=os.getenv("BROKER_URL"),
             include=["main"])

app.conf.beat_schedule = {
    # sends out an email every day at 5:30 PM UTC (9:30 AM Pacific Time)
    "trigger-email-notifications": {
        "task": "send_email",
        "schedule": crontab(minute="30", hour="17")
    }
}
