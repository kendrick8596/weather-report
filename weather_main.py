# Python project that will use an API key for Openweather and return the current weather for a location

import os
from dotenv import load_dotenv
from client import WeatherClient
from report import WeatherReport

# Load the .enf file for variables
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def main():
    # Create the instance and pass the inputs as arguments
    client = WeatherClient(api_key=API_KEY)
    user_city = input("Enter the city: ")
    user_state = input("Enter State: ")


    my_client = client.weather_fetch(user_city, user_state)
    #print(my_client)

    report = WeatherReport(my_client)
    print(report)

if __name__ == "__main__":
    main()