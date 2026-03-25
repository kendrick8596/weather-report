import requests

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