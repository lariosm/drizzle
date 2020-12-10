# Baltazar Ortiz
import os
from parser import phoneMessage
from weather_email import sendMessage
from getData import getWeatherData

api_key = os.getenv('API_KEY')
sender_email = os.getenv('FROM_EMAIL')
receiver_email = os.getenv('SEND_EMAIL') 
password = os.getenv('PASSWORD')

data = getWeatherData(api_key)
premessage = """Subject: Weather Update (Baltazar Ortiz)

"""
message = phoneMessage(data, premessage)
sendMessage(message, sender_email, receiver_email, password)
