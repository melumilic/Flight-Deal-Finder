import os
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
    
    def update_entry(
        self,
    ):
        pass

    def delete_entry(self):
        pass

    def get_entry(self):
        pass

    # This class is responsible for talking to the Google Sheet.
