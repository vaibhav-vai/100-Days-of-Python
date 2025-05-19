import requests
from datetime import datetime
import os

GENDER = "Male"
WEIGHT_KG = 80.4
HEIGHT_CM = 160
AGE = 24

APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]

nutrition_endpoint = "https://trackapi.nutritionix.com//v2/natural/exercise"
sheet_endpoint = os.environ["ST_ENDPOINT"]

exercise = input("Tell me which exercise you did?")

nutrition_params = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url=nutrition_endpoint, json=nutrition_params, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
    }
    }

sheet_response = requests.post(
    url=sheet_endpoint,
    json=sheet_input,
    auth=(
      os.environ["ST_USERNAME"],
      os.environ["ST_PASSWORD"],
  ))
print(sheet_response.text)