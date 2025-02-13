import requests
import matplotlib.pyplot as plt

def get_weather_report(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        return {
            'city': city_name,
            'weather': weather,
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed
        }
    else:
        return None

def save_weather_report(report, filename):
    with open(filename, 'a') as file:
        file.write(f"Weather in {report['city']}:\n")
        file.write(f"Description: {report['weather']}\n")
        file.write(f"Temperature: {report['temperature']}°C\n")
        file.write(f"Humidity: {report['humidity']}%\n")
        file.write(f"Wind Speed: {report['wind_speed']} m/s\n")
        file.write("\n")

def plot_weather_data(reports):
    cities = [report['city'] for report in reports]
    temperatures = [report['temperature'] for report in reports]
    plt.bar(cities, temperatures)
    plt.xlabel('Cities')
    plt.ylabel('Temperature (°C)')
    plt.title('Weather Report')
    plt.show()

def main():
    api_key = '012cf7d257b824ebb662b611b9bcd11d'  # Replace with your OpenWeatherMap API key
    reports = []
    while True:
        city_name = input("Enter the city name (or 'exit' to quit): ")
        if city_name.lower() == 'exit':
            break
        weather_report = get_weather_report(city_name, api_key)
        if weather_report:
            print(f"Weather in {weather_report['city']}:")
            print(f"Description: {weather_report['weather']}")
            print(f"Temperature: {weather_report['temperature']}°C")
            print(f"Humidity: {weather_report['humidity']}%")
            print(f"Wind Speed: {weather_report['wind_speed']} m/s")
            reports.append(weather_report)
            save_weather_report(weather_report, '../data/weather_reports.txt')
        else:
            print("Failed to retrieve weather data. Please check the city name and API key.")

    if reports:
        plot_weather_data(reports)

if __name__ == "__main__":
    main()