class WeatherReport:
   
    def __init__(self, data_dict):
        self.temp = data_dict['current']['temp_f']
        self.humidity = data_dict['current']['humidity']
        self.description = data_dict['current']['condition']['text']
        self.wind_speed = data_dict['current']['wind_mph']
        self.city = data_dict['location']['name']
        self.state = data_dict['location']['region']

    def __str__(self):
        return (
                f"\033[1mCURRENT WEATHER:\033[0m {self.city}, {self.state}\n"
                f"\033[1mTemperature:\033[0m {self.temp} °F\n"
                f"\033[1mHumidity:\033[0m {self.humidity}%\n"
                f"\033[1mConditions:\033[0m {self.description}"
        )