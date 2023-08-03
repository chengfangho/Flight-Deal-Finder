import requests

ENDPOINT = "https://api.sheety.co/2f6a8e37ea876dc9b428ce34857ca038/flightDeals/prices"
TOKEN = "Bearer J72@4DEJD$P"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self):
        self.data = {}

    def get_data(self):
        headers = {
            "Authorization": TOKEN
        }
        response = requests.get(url=ENDPOINT, headers=headers)
        data = response.json()["prices"]
        self.data = data
        return self.data
    
    def update_code(self):
        headers = {
            "Authorization": TOKEN
        }
        for city in self.data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{ENDPOINT}/{city['id']}",
                headers=headers,
                json=new_data
            )