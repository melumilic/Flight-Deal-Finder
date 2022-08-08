from mimetypes import init
import os
from tokenize import String
from xmlrpc.client import Boolean
import requests
from twilio.rest import Client

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.environ.get("TWILIO_VIRTUAL_NUMBER")
TWILIO_VERIFIED_NUMBER = os.environ.get("TWILIO_VERIFIED_NUMBER")

class NotificationManager:
    __TWILIO_API_SID = os.environ["TWILIO_SID"]
    __TWILIO_AUTH_KEY = os.environ["TWILIO_AUTH_TOKEN"]
    #__TWILIO_ENDPOINT = 
    def __init__(self) -> None:
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN);

    def send_message(self,message:String):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )
        print(message.sid)
    #This class is responsible for sending notifications with the deal flight details.
