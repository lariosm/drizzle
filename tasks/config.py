# import os

'''
=======NOTICE=======
config.py currently serves as a placeholder which
will be used to configure broker settings in the
future when the app is deployed to the cloud.
'''

'''
example:

BROKER_USER = os.getenv("BROKER_USER")
BROKER_PASSWORD = os.getenv("BROKER_PASSWORD")
BROKER_HOST = os.getenv("BROKER_HOST")
BROKER_PORT = os.getenv("BROKER_PORT")
BROKER_VHOST = os.getenv("BROKER_VHOST")

CELERY_BROKER_URL = f"amqp://{BROKER_USER}:{BROKER_PASSWORD}@{BROKER_HOST}\
    :{BROKER_PORT}/{BROKER_VHOST}"
'''
