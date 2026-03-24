# Python project that will use an API key for Openweather and return the current weather for a location

import requests
import json
import os
from dotenv import load_dotenv 

# Load the .enf file for variables
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

class WeatherClient:
    def __init__(self, api_key, base_url="http://api.weatherapi.com/v1/current.json", unit_system="imperial"):
        self.api_key = api_key
        self.base_url = base_url
        self.unit_system = unit_system

    def weather_fetch(self, city, state):
        parameters = {'q': f"{city},{state}", 'key': self.api_key}
        response = requests.get(self.base_url, params=parameters)
        #print(response)
        return response.json()
    
class WeatherReport:
    def __init__(self, data_dict):
        self.temp = data_dict['current']['temp_f']
        self.humidity = data_dict['current']['humidity']
        self.description = data_dict['current']['condition']['text']
        self.wind_speed = data_dict['current']['wind_mph']
        self.city = data_dict['location']['name']
        self.state = data_dict['location']['region']

    def __str__(self):
        return f"\033[1mCURRENT WEATHER:\033[0m {self.city}, {self.state}\n\033[1mTemperature:\033[0m {self.temp} °F\n\033[1mHumidity:\033[0m {self.humidity}%\n\033[1mConditions:\033[0m {self.description}"

# Create the instance and pass the inputs as arguments
client = WeatherClient(api_key=API_KEY)
user_city = input("Enter the city: ")
user_state = input("Enter State: ")


my_client = client.weather_fetch(user_city, user_state)
#print(my_client)

report = WeatherReport(my_client)
#print(f"It is currently {report.temp} °F with humidty of {report.humidity}% in {report.city}, {user_state} wind speed of {report.wind_speed} mph with {report.description} skies.")
print(report)








'''
def city_zip_input(prompt):
        user_input = input(prompt)
        return user_input
# Testing Testing Testing
client = WeatherClient(api_key=API_KEY)
my_client = client.weather_fetch("Dallas", "75249")
print(my_client)


while True:
    user_zip = input("Enter the zipcode: ")
    if len(user_zip) != 5:
        print("Invalid Zipcode")
    elif len(user_zip) == 5 and user_zip.isdigit():
        break

my_client = client.weather_fetch(user_city, user_zip)
print(my_client)

'''