import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

print("Basic Weather App")

city = input("Enter city name: ").strip()

if city == "":
    print("Please enter a city name.")

else:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if response.status_code == 200:

            temperature_c = data["main"]["temp"]
            temperature_f = (temperature_c * 9 / 5) + 32

            print("\nWeather Report")
            print("City:", data["name"])
            print("Temperature:", round(temperature_c, 2), "°C")
            print("Temperature:", round(temperature_f, 2), "°F")
            print("Feels like:", data["main"]["feels_like"], "°C")
            print("Humidity:", data["main"]["humidity"], "%")
            print("Weather:", data["weather"][0]["description"])
            print("Wind Speed:", data["wind"]["speed"], "m/s")

        elif response.status_code == 401:
            print("Invalid API key.")

        elif response.status_code == 404:
            print("City not found.")

        else:
            print("Something went wrong. Please try again.")

    except requests.exceptions.Timeout:
        print("The request timed out. Please try again.")

    except requests.exceptions.RequestException:
        print("Network error. Please check your internet connection.")