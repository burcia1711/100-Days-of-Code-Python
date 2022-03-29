import requests
from twilio.rest import Client

api_key = "YOUR_KEY"
account_sid = "YOUR_ACCOUNT_ID"
auth_token = "AUTHENTICATION_TOKEN"

parameters = {
    "lat": 39.896519,
    "lon": 32.861969,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_ids = []
will_rain = False

for i in range(0, 12):
    weather_ids.append(weather_data["hourly"][i]["weather"][0]["id"])

for cond_id in weather_ids:
    if cond_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bugün yağmur yağacak.️"
             " Yanına şemsiye almayı unutma ☔",
        from_="+12677543546",
        to="+905333305601",
    )
    print(message.status)
