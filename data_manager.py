import requests

Sheety_API = "https://api.sheety.co/f4406f51c5fa464521d92d5eeec5ebd9/flightDeals/prices"

class DataManager:

    def __init__(self):
        self.destination = {}

    def get_data(self):
        response = requests.get(url=Sheety_API)
        self.destination = response.json()['prices']
        return self.destination
    def update_data(self):
        for city in self.destination:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{Sheety_API}/{city['id']}",
                json=new_data
            )
            #print(response.text)