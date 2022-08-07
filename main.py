from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
# from notification_manager import NotificationManager
import os

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# test = DataManager()
# test.add_entry("Los Angeles")

flight_search_test = FlightSearch()
print(flight_search_test.get_iata_code("London"))