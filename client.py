import requests
import json

class WeatherClient:
    def __init__(self, api_key, base_url="http://api.weatherapi.com/v1/current.json", unit_system="imperial"):
        self.api_key = api_key
        self.base_url = base_url
        self.unit_system = unit_system

    def weather_fetch(self, city, state):
        if not city or not state:
            return {"error": "invalid_input", "message": "City and state are required!"}
        
        parameters = {'q': f"{city},{state}", 'key': self.api_key}

        try:
            response = requests.get(self.base_url, params=parameters, timeout=10)       # set a timeout of 10 seconds for network issues

            # check for bad HTTP status codes (4xx or 5xx)
            response.raise_for_status()

            # parse the json if successful
            data = response.json()
            
            # *** CREATE STRICT VALIDATION FOR CITY AND STATE ***
            if "error" in data:
                return {"error": "api_error", "message": data["error"].get("message")}
            
            # get nested dictionary
            location_dict = data.get("location", {})

            # extract name and region strings from the dictionary with empty strings
            returned_city = location_dict.get("name", "")
            returned_state = location_dict.get("region", "")

            # compare the city and state string to the returned city and state string
            if city.lower() not in returned_city.lower():
                return {"error": "mismatch", "message": f"No exact match for '{city}'. (Found '{returned_city}' instead)"}
            if state.lower() not in returned_state.lower():
                return {"error": "mismatch", "message": f"No exact match for '{state}'. (Found '{returned_state}' instead)"}

            return data
        
        except requests.exceptions.ConnectionError as e:
            # handle network problems
            return {"error": "connection timeout", "message": str(e)}
        except requests.exceptions.Timeout as e:
            # handle timeouts
            return {"error": "timeout", "message": str(e)}
        except requests.exceptions.HTTPError as e:
            # handle http status codes
            return {
                "error": "http_error",
                "status_code": response.status_code,
                "response": response.text
            }
        except json.JSONDecodeError:
            # handle not valid json
            return {
                "error": "error decoding json", "message": str(e)
            }
        except requests.exceptions.RequestException as e:
            # catch general errors
            return {"error": "unexpected request", "message": str(e)}
