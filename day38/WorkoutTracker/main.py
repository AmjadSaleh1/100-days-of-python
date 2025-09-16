import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 168
AGE = 30
SHEET_URL = "https://api.sheety.co/6348fc7fae222c67d4dd4c567d6c5827/myWorkoutsDemo/workouts"
USERNAME = os.environ["USERNAME_AUTH"]
PASSWORD = os.environ["PASSWORD_AUTH"]
API_KEY = os.environ["API_KEY_AUTH"]
API_ID = os.environ["API_ID_AUTH"]


headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}
exercise_text = input("Tell me which exercises you did: ")

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(
    url="https://trackapi.nutritionix.com/v2/natural/exercise",
    json=params,
    headers=headers
)
result = response.json()
response.raise_for_status()

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(SHEET_URL,
                                   json=sheet_inputs,
                                   auth=(
                                       USERNAME,
                                       PASSWORD
                                   )
                                   )
    print(sheet_response.text)
