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
    my_client = WeatherClient(api_key=API_KEY)
    user_city = input("Enter the city: ")
    user_state = input("Enter State: ")

    result = my_client.weather_fetch(user_city, user_state)

    if "error" in result:
        error_msg = result.get("message", "Unknown error occured!")
        print(f"Error: {error_msg}")
    else:
        report = WeatherReport(result)
        print(report)

if __name__ == "__main__":
    main()