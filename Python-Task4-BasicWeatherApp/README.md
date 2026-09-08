# Basic Weather App

This is a simple Python weather application that uses the OpenWeather API to fetch and display current weather information for a city entered by the user.

## How it works

1. The user enters the name of a city.
2. The program sends a request to the OpenWeather API.
3. The API returns the current weather data for the city.
4. The program processes the received data.
5. The weather information is displayed in the terminal.

## Weather Information Displayed

- City name
- Temperature
- Feels like temperature
- Humidity
- Weather description

## Technologies Used

- Python
- Requests library
- OpenWeather API

## How to Run

1. Open the `basic_weather_app.py` file.
2. Make sure the `requests` library is installed.
3. Add your OpenWeather API key to the program.
4. Run the Python program.
5. Enter the name of a city when prompted.
6. The current weather information will be displayed.

## Example Output

```text
Weather Report
City: Karimnagar
Temperature: 24.11 °C
Feels Like: 24.5 °C
Humidity: 78 %
Weather: overcast clouds
```

## Features

- Fetches real-time weather information.
- Allows the user to search for any city.
- Displays temperature in Celsius.
- Displays feels-like temperature.
- Displays humidity.
- Displays weather conditions.
- Uses the OpenWeather API.
- Simple and beginner-friendly Python application.

## Error Handling

If the entered city cannot be found or the API request fails, the program displays an error message instead of crashing.

## Conclusion

The Basic Weather App demonstrates how Python can communicate with a weather API and process JSON data to provide useful real-time weather information to the user.