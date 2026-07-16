from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import os


load_dotenv()
SHEETY_PRICES_ENDPOINT=os.environ["SHEETY_PRICES_ENDPOINT"]

class DataManager:
    def __init__(self):
        self._user = os.environ.get("SHEETY_USERNAME")
        self._password = os.environ.get("SHEETY_PASSWORD")
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.users_endpont = os.environ["SHEETY_USERS_ENDPOINT"]
        self.destination_data = {}
        self.customer_data = {}
        
    def get_destination_data(self):

        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth = self._authorization)
        self.destination_data = response.json()["prices"]
        return self.destination_data
    
    def update_lowest_price(self,row_id, new_price):
        new_data = {
            "prices":{
                "lowestPrice": new_price
            }

        }
        requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{row_id}", json=new_data, auth= self._authorization)

    def get_customer_emails(self):
        response = requests.get(url= self.users_endpont, auth=self._authorization)
        self.customer_data = response.json()["users"]
        return self.customer_data



