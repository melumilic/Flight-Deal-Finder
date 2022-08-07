from email import header
import os
import requests
import json

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.__TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]
        self.__TEQUILA_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
        self.__TEQUILA_LOCATIONS_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
        self.__TEQUILA_HEADERS = {"apikey": self.__TEQUILA_API_KEY}

    def get_iata_code(self, location):
        params = {
            "term":location,
            "location_types":"city"
        }
        request = requests.get(
            url=self.__TEQUILA_LOCATIONS_ENDPOINT, params=params, headers=self.__TEQUILA_HEADERS
        )
        city_json = request.json()["locations"]
        #print(request.text)
        return city_json[0]["code"]
