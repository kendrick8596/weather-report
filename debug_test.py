from client import WeatherClient

client = WeatherClient("YOUR_API_KEY")
print(client.weather_fetch("Dallas", "TX"))
