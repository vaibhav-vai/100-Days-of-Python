import requests
from twilio.rest import Client


api_key = 'openweathermap_api_key'
account_sid = 'twilio_sid'
auth_token = 'twilio_auth_token'

MY_LAT = 51.958660
MY_LONG = 85.960197

parameters = {
    "lat" : MY_LAT,
    "lon" : MY_LONG,
    "appid" : api_key,
    "cnt": 4
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
#print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today bring Umbrella",
        from_='+16203123740',
        to='+917277682083'
    )
    print(message.status)
