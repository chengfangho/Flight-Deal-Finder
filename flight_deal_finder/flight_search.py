from flight_data import FlightData
import requests

ENDPOINT = "https://api.tequila.kiwi.com"
API_KEY = "RrtpxFWoJ_TVdwtrCoDXZLS3_5c8ZNwZ"

class FlightSearch:
    
    def __init__(self):
        pass
    
    def get_code(self, city_name):
        headers = {
            "apikey": API_KEY
        }
        params = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(
            url=f"{ENDPOINT}/locations/query",
            headers=headers,
            params=params
        )
        return response.json()["locations"][0]["code"]
    
    def search_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {
            "apikey": API_KEY
        }
        params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }
        response = requests.get(
            url=f"{ENDPOINT}/v2/search",
            headers=headers,
            params=params
        )
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        flight_data = FlightData(
            price=data["price"], 
            origin_city=data["route"][0]["cityFrom"], 
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["local_departure"].split("T")[0],
            return_date=data["local_departure"].split("T")[0]
        )
        return flight_data