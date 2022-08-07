from email import header
import os
from re import search
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
        self.__search_result_data = None

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
    ):
        search_params = {
            "fly_from": iata_code,
            "fly_to": destination_airport,
            "date_from": date_from,
            "date_to": date_to,
            "curr": "USD",
            "nights_in_dst_from":7,
            "nights_in_dst_to":10,
            "one_for_city":1,
            #"flight_type":"round",
            "max_stopovers":0
        }
        search_request = requests.get(
            url=self.__TEQUILA_SEARCH_ENDPOINT,
            params=search_params,
            headers=self.__TEQUILA_HEADERS,
        )
        #print(search_request.text)
        with open("search_results.json", "w") as f:
            json.dump(search_request.json(), f)
        with open("search_results.json") as f:
            search_json = json.load(f)
        self.__search_result_data = search_json


    def get_cheapest_flight(
        self,
        iata_code: String,
        destination_airport: String,
        date_from: String,
        date_to: String,
    ) -> FlightData:
        # with open("search_results.json") as f:
        #     search_json = json.load(f)
        if self.__search_result_data is None:
            self.get_flights(
                iata_code=iata_code,
                destination_airport=destination_airport,
                date_from=date_from,
                date_to=date_to,
            )
        #search_result = search_json["data"][0]
        search_result = self.__search_result_data["data"][0]
        flight_data = FlightData(
            price=search_result["price"],
            origin_city=search_result["cityFrom"],
            origin_airport=search_result["cityCodeFrom"],
            destination_city=search_result["cityTo"],
            destination_airport=search_result["cityCodeTo"],
            out_date=search_result["route"][0]["local_departure"],
            return_date=search_result["route"][1]["local_departure"]
        )
        return flight_data

