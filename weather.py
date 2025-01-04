import requests
from pprint import pprint


API_key = '929ac35f81ead7c02a6d1139ec3228b4'

city = input("Enter name of city : ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)