import requests

api_key = "30d4741c779ba94c470ca1f63045390a"

def get_weather_data(city_name):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&APPID={api_key}")
    return response.json()

def display_weather_info(weather_data):
    if weather_data['cod'] == '404':
        print("City not found")
    else:
        main = weather_data['weather'][0]['main']
        temp = round(weather_data['main']['temp'])
        feels_like = round(weather_data['main']['feels_like'])
        pressure = weather_data['main']['pressure']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        wind_deg = weather_data['wind']['deg']

        print(f"The weather in {weather_data['name']} is {main}")
        print(f"Temperature: {temp}°C")
        print(f"Feels Like: {feels_like}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Wind Degree: {wind_deg}°")

if __name__ == "__main__":
    user_input = input("Enter the city name: ")
    weather_data = get_weather_data(user_input)
    display_weather_info(weather_data)
