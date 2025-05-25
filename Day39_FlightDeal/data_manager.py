import os
import requests
from pprint import pprint
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

sheety_endpoint = "https://api.sheety.co/03f78596e3625dceb632e6e63d4a873c/flightDeals/prices"

class DataManager:
    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    #This class is responsible for talking to the Google Sheet.
    def get_destination_data(self):
        response = requests.get(url=sheety_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price":
                    {
                        "iataCode": city["iataCode"]
                    }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data,
                auth = self._authorization
            )
            print(response.text)