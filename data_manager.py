import os
from typing import Dict
import requests


class DataManager:
    def __init__(self) -> None:
        self.__SHEETY_API_ENDPOINT = (
            "https://api.sheety.co/0b894557eeaf40d648330c8d67568854/flightDeals/prices"
        )
        self.__SHEETY_AUTH_TOKEN = os.environ["SHEETY_AUTH_TOKEN"]
        self.__SHEETY_HEADER = {
            "Authorization": "Bearer " + self.__SHEETY_AUTH_TOKEN,
            "Content-Type": "application/json"
        }
        pass

    def add_entry(self, city):
        data = {"price": {"city": city}}
        request = requests.post(
            url=self.__SHEETY_API_ENDPOINT, json=data, headers=self.__SHEETY_HEADER
        )
        print(request.text)
        pass
    
    def get_sheet(self) -> Dict:
        request = requests.get(url=self.__SHEETY_API_ENDPOINT,headers=self.__SHEETY_HEADER)
        print(request.text)
        sheet_json = request.json()
        print(sheet_json)
        return sheet_json

    def update_entry(
        self,
    ):
        pass

    def delete_entry(self):
        pass


    # This class is responsible for talking to the Google Sheet.
