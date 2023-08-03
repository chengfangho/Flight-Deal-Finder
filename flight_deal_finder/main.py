#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from datetime import datetime, timedelta

ORIGIN_CITY_IATA = "SFO"

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_data()

for row in sheet_data:
    row["iataCode"] = flight_search.get_code(row["city"])
pprint(f"sheet_data:\n {sheet_data}")

data_manager.data = sheet_data
data_manager.update_code()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    data = flight_search.search_flight(ORIGIN_CITY_IATA, destination["iataCode"], tomorrow, six_month_from_today)
    if data != None:
        print(f"{data.destination_city}: {data.price}")
