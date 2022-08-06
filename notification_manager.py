import os
from xmlrpc.client import Boolean
import requests
from twilio.rest import Client

class NotificationManager:
    __TWILIO_API_SID = os.environ["TWILIO_SID"]
    __TWILIO_AUTH_KEY = os.environ["TWILIO_AUTH_TOKEN"]
    __TWILIO_ENDPOINT = 
    def __init__(self) -> None:
        pass
    def send_message(self) -> Boolean:
        requests.post()
    #This class is responsible for sending notifications with the deal flight details.
