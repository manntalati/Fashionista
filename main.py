import requests
import geocoder
import random

g = geocoder.ip('me')
endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "{API_KEY}"
account_sid = "{ACCOUNT_SID}"
auth_token = "{AUTH_TOKEN}"

parameters = {
    "lat": g.lat,
    "lon": g.lng,
    "appid": api_key,
    "units": "imperial"
}
rain = False
response = requests.get(url=endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_id = weather_data['weather'][0]['id']
atmosphere = weather_data['weather'][0]['main']
temperature = weather_data['main']['temp']

top = ""
bottom = ""
umbrella = False
color_schemes = []
used_color_schemes = []
long_sleeve_top = ["Sweatshirt", "Shirt", "Hoodie", "Crewneck", "Jacket"]
long_sleeve_bottom = ["Jeans", "Sweats", "Cargo Pants"]
short_sleeve_top = ["Tanktop", "T-Shirt", "Short Sleeve Shirt"]
short_sleeve_bottom = ["Shorts", "Cargo Shorts"]

# Thunderstorm 200s
if 200 <= weather_id <= 232:
    top = long_sleeve_top[random.randint(0, 4)]
    bottom = "Jeans/Pants"
    umbrella = True
    rain = True

# Drizzle 300s
elif 300 <= weather_id <= 321:
    top = "Sweatshirt/Hoodie"
    bottom = "Jeans/Pants"
    umbrella = True
    rain = True

# Rain 500s
elif 500 <= weather_id <= 531:
    top = "Sweatshirt/Hoodie"
    bottom = "Jeans/Pants"
    umbrella = True
    rain = True

# Snow 600s
elif 600 <= weather_id <= 622:
    top = "Sweatshirt/Hoodie"
    bottom = "Jeans/Pants"
    umbrella = True
    rain = True

# Atmosphere 700s
elif 700 <= weather_id <= 781:
    top = "Sweatshirt/Hoodie"
    bottom = "Jeans/Pants"
    umbrella = True
    rain = True

# Clear 800
elif weather_id == 800:
    top = "Sweatshirt/Hoodie"
    bottom = "Jeans/Pants"
    umbrella = True
    rain = True

# Clouds 800s
elif 801 <= weather_id <= 804:
    top = "Sweatshirt/Hoodie"
    bottom = "Jeans/Pants"
    umbrella = True
    rain = True