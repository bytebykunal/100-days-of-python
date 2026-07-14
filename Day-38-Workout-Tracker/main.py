import requests
from datetime import datetime
import os


GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 183
AGE = 18
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")


sheet_endpoint = "https://api.sheety.co/9b00e8d3e0ac97235a43c690a8bbcda5/workoutTracking/sheet1"

NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY= os.environ.get("NUTRITIONIX_API_KEY")
exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

nutritionix_headers = {
    "x-app-id": NUTRITIONIX_APP_ID ,
    "x-app-key": NUTRITIONIX_API_KEY,
    "Content-Type": "application/json",
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(url= exercise_endpoint, json = parameters, headers=nutritionix_headers)
response.raise_for_status()
result = response.json()


sheety_headers = {
    "Authorization":  f"Bearer {SHEETY_TOKEN}"
}

now = datetime.now()

for exercise in result["exercises"]:
    data = {
        "sheet1": {
            "date": now.strftime("%Y/%m/%d"),
            "time": now.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],

        }
    }

    data_upload = requests.post(url= sheet_endpoint, json=data, headers=sheety_headers)
    data_upload.raise_for_status()