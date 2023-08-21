
# The Weather app
# Write a console application which takes as an input a city name and returns current weather in the format of your choice.
#  For the current task, you can choose any weather API or website or use openweathermap.org 

# data source - http://api.weatherapi.com
# API request example - http://api.weatherapi.com/v1/current.json?key=<YOUR_API_KEY>&q=London

import requests

# defining api key and base_url
my_api_key = 'a706560a8d5d40d8ab6101938232108'
base_url = 'http://api.weatherapi.com/v1/current.json?'

# defining city
city = 'Dubrovnik'

# calling API to retrive current weather data for the city
weather_current = requests.get('http://api.weatherapi.com/v1/current.json?', params ={
"key":{my_api_key},'q':{city}})

# printing responce details
print(weather_current.status_code, weather_current.reason)
print(weather_current.json())