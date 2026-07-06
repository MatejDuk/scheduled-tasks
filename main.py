import requests
import json
import os
from twilio.rest import Client

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

api_key = os.environ.get("OWM_API_KEY")

parameters = {
    "lat": 48.219238,
    "lon": 18.606501,
    "cnt":4,
    "appid": "44c39425cf7c27ec667a65208d532239",
}


response = requests.get(url = "https://api.openweathermap.org/data/2.5/forecast", params = parameters)
response.raise_for_status()
rain = False
for i in range(4):
    weather_id = response.json()["list"][i]["weather"][0]["id"]
    if weather_id <= 700:
        rain = True

if rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is going to rain today! Remember to bring an umbrella!",
        from_="+19562017366",
        to="+421917334675",
    )
    print(message.body)
