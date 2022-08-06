from email import header
import os
import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.__TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]
        self.__TEQUILA_ENDPOINT = "tequila-api.kiwi.com/v2/search"
        self.__TEQUILA_HEADERS = {"apikey": self.__TEQUILA_API_KEY}
        pass

    def get_flight_data(
        self,
        fly_from,
        fly_to,
        date_from,
        date_to,
        return_from,
        return_to,
        adults,
        price_from,
        price_to,
    ):
        pass

    def check_flights(self):
        pass

    def get_iata_code(self, location):
        params = {}
        request = requests.get(
            url=self.__TEQUILA_ENDPOINT, params=params, headers=self.__TEQUILA_HEADERS
        )
        pass
