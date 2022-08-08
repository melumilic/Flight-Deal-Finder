import json
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch

# from notification_manager import NotificationManager
import os

from notification_manager import NotificationManager

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# test = DataManager()
# test.add_entry("Los Angeles")

# flight_search_test = FlightSearch()
# print(flight_search_test.get_iata_code("London"))

data_manager = DataManager()
# data_manager.add_entry(city="Taipei")
# flight_sheet = data_manager.get_sheet()
# with open("flight_list.json","w") as f:
#     json.dump(flight_sheet, f)
with open("flight_list.json") as f:
    flight_sheet = json.load(f)
print(flight_sheet)
flight_sheet = flight_sheet["prices"]
index = 2
for entry in flight_sheet:
    search_result = FlightSearch().get_cheapest_flight(
        iata_code="LAX",
        destination_airport=entry["iataCode"],
        date_from="01/09/2022",
        date_to="11/09/2022",
    )
    DataManager().update_entry_price(index=index, price=search_result.price)
    if search_result.price < 200:
        NotificationManager().send_message(
            message=f"Flight from {search_result.origin_airport} to {search_result.destination_airport} departing {search_result.out_date} only ${search_result.price}"
        )
    index += 1

# data_manager.update_entry(index=2,iata_code=FlightSearch().get_iata_code("TPE"))
# FlightSearch().get_flights(
#     iata_code="LAX",
#     destination_airport="RNO",
#     date_from="08/08/2022",
#     date_to="02/09/2022",
# )

# with open("search_results.json") as f:
#     search_json = json.load(f)

# print(search_json["data"][0]["price"])

# search_result = FlightSearch().get_cheapest_flight(
#     iata_code="LAX",
#     destination_airport="RNO",
#     date_from="08/08/2022",
#     date_to="02/09/2022",
# )

# print(search_result)
