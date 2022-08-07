from email import header
import os
from tokenize import String
import requests
import json
import datetime as dt

from flight_data import FlightData


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.__TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]
        self.__TEQUILA_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
        self.__TEQUILA_LOCATIONS_ENDPOINT = (
            "https://tequila-api.kiwi.com/locations/query"
        )
        self.__TEQUILA_HEADERS = {"apikey": self.__TEQUILA_API_KEY}
        self.flight_data = FlightData()
        self.__search_result_data = {}

    def get_iata_code(self, location):
        params = {"term": location, "location_types": "city"}
        request = requests.get(
            url=self.__TEQUILA_LOCATIONS_ENDPOINT,
            params=params,
            headers=self.__TEQUILA_HEADERS,
        )
        city_json = request.json()["locations"]
        # print(request.text)
        return city_json[0]["code"]

    def get_flights(
        self,
        iata_code: String,
        destination_airport: String,
        date_from: String,
        date_to: String,
        **kwargs
    ):
        kwargs = {
            "price": "price",
            "origin_city": "Los Angeles",
            "origin_airport": "LAX",
            "destination_city": "Taipei",
            "destination_airport": "TPE",
            "date_from": dt.datetime.now().strftime("%d/%m/%Y"),
            "date_to": "one way",
        }
        search_params = {
            "fly_from": iata_code,
            "fly_to": destination_airport,
            "date_from": date_from,
            "date_to": date_to,
            "curr": "USD",
        }
        search_request = requests.get(
            url=self.__TEQUILA_SEARCH_ENDPOINT,
            params=search_params,
            headers=self.__TEQUILA_HEADERS,
        )
        print(search_request.text)
        with open("search_results.json", "w") as f:
            json.dump(search_request.json(), f)
        with open("search_results.json") as f:
            search_json = json.load(f)
        search_json = search_json["data"][0]

        pass

    def get_search_result(self)->FlightData:
        self.flight_data = FlightData()