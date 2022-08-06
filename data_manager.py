import os


import os
from tokenize import String
import requests

class DataManager:
    __SHEETY_API_ENDPOINT = "https://api.sheety.co/0b894557eeaf40d648330c8d67568854/flightDeals/prices"
    __SHEETY_AUTH_TOKEN = os.environ["SHEETY_AUTH_TOKEN"]
    __SHEETY_HEADER = {"Authorization":__SHEETY_AUTH_TOKEN}

    def __init__(self) -> None:
        pass

    def update_data(self) -> String:
        
    #This class is responsible for talking to the Google Sheet.
    pass