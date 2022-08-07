import os
from tokenize import String
from typing import Dict
import requests
from flight_search import FlightSearch


class DataManager:
    def __init__(self) -> None:
        self.__SHEETY_API_ENDPOINT = (
            "https://api.sheety.co/0b894557eeaf40d648330c8d67568854/flightDeals/prices"
        )
        self.__SHEETY_AUTH_TOKEN = os.environ["SHEETY_AUTH_TOKEN"]
        self.__SHEETY_HEADER = {
            "Authorization": "Bearer " + self.__SHEETY_AUTH_TOKEN,
            "Content-Type": "application/json",
        }
        pass

    def add_entry(self, city: String):
        data = {"price": {"city": city, "iataCode": FlightSearch().get_iata_code(city)}}
        request = requests.post(
            url=self.__SHEETY_API_ENDPOINT, json=data, headers=self.__SHEETY_HEADER
        )
        print(request.text)
        pass

    def get_sheet(self) -> Dict:
        request = requests.get(
            url=self.__SHEETY_API_ENDPOINT, headers=self.__SHEETY_HEADER
        )
        print(request.text)
        sheet_json = request.json()
        print(sheet_json)
        return sheet_json

    def update_entry_price(self, index: int, price=None):
        if price is None:
            return
        update_data = {"price": {"lowestPrice": price}}

        request = requests.put(
            url=self.__SHEETY_API_ENDPOINT + f"/{index}",
            json=update_data,
            headers=self.__SHEETY_HEADER,
        )
        print(request.text)

    def delete_entry(self):
        pass

    # This class is responsible for talking to the Google Sheet.
