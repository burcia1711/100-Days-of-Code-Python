import requests

SHEETY_ENDPOINT = "https://api.sheety.co/9c34cd8b4465e5c927671a04cb48fa35/flightDeals/prices"


# This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.sheet_data = {}

    def get_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.sheet_data = data["prices"]
        return self.sheet_data

    def update_codes(self):
        for city in self.sheet_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
