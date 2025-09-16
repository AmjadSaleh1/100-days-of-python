import requests
import os
from twilio.rest import Client

account_sid = os.getenv("TWILIO_ACOUNT_SID")
auth_token = os.getenv("auth_token")
api_key = os.getenv("api_key")
getenv(
parameters = {
    "lat": 46.035940,
    "lon": 9.124550,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for item in weather_data['list']:
    condition_code = item["weather"][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            body="its going to rain today. remember umberlla ",
            from_="+14159388935",
            to="+18777804236",
        )
    print(message.status)

