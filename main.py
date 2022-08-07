import json
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch

# from notification_manager import NotificationManager
import os

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# test = DataManager()
# test.add_entry("Los Angeles")

# flight_search_test = FlightSearch()
# print(flight_search_test.get_iata_code("London"))

data_manager = DataManager()
data_manager.add_entry(city="Taipei")
flight_list = data_manager.get_sheet()
with open("flight_list.json","w") as f:
    json.dump(flight_list)
with open("flight_list.json") as f:
    flight_list = f
print(flight_list)
#data_manager.update_entry(index=2,iata_code=FlightSearch().get_iata_code("TPE"))
# FlightSearch().get_flights(
#     iata_code="LAX",
#     destination_airport="RNO",
#     date_from="08/08/2022",
#     date_to="02/09/2022",
# )

# with open("search_results.json") as f:
#     search_json = json.load(f)

#print(search_json["data"][0]["price"])

# search_result = FlightSearch().get_cheapest_flight(
#     iata_code="LAX",
#     destination_airport="RNO",
#     date_from="08/08/2022",
#     date_to="02/09/2022",
# )

# print(search_result)