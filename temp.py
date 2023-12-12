import requests


cities = [
'Andorra la Vella', 'Tirana', 'Vienna', 'Minsk', 'Brussels', 'Sarajevo', 'Sofia',
'Zagreb', 'Nicosia', 'Prague', 'Copenhagen', 'Tallinn', 'Helsinki', 'Paris',
'Berlin', 'Athens', 'Budapest', 'Reykjavik', 'Dublin', 'Rome', 'Pristina',
'Riga', 'Vaduz', 'Vilnius', 'Luxembourg City', 'Skopje', 'Valletta', 'Chisinau',
'Monaco', 'Podgorica', 'Amsterdam', 'Oslo', 'Warsaw', 'Lisbon', 'Bucharest',
'Moscow', 'San Marino', 'Belgrade', 'Bratislava', 'Ljubljana', 'Madrid', 'Stockholm',
'Bern', 'Ankara', 'Kyiv', 'London', 'Hamburg', 'Milan', 'Barcelona', 'Vienna', 'Prague', 'Copenhagen', 'Athens',
'Budapest', 'Reykjavik', 'Dublin', 'Rome', 'Riga', 'Luxembourg City', 'Oslo',
'Warsaw', 'Lisbon', 'Bucharest', 'Moscow', 'Amsterdam', 'Madrid', 'Stockholm',
'Brussels', 'Berlin', 'Paris', 'London'
]


def get_weather_data(api_key, cities, hottest=True):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    temperature_data = {}

    for city in cities:
        params = {
            "q": city,
            "units": "metric",
            "appid": api_key,
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            weather_info = response.json()
            temperature = weather_info['main']['temp']
            temperature_data[city] = temperature

    sorted_temperatures = sorted(temperature_data.items(), key=lambda x: x[1], reverse=not hottest)
    top_5 = dict(sorted_temperatures[:5])

    return top_5

def main():
    api_key = "e8081ab0568ec8b77c4318ba87cece26"

    user_choice = input("Enter 'hot' for hottest capitals or 'cold' for coldest capitals: ").lower()
    hottest = False if user_choice == 'hot' else True

    top_cities = get_weather_data(api_key, cities, hottest=hottest)

    if hottest:
        print("Top 5 Hottest Capitals in Europe:")
    else:
        print("Top 5 Coldest Capitals in Europe:")

    for city, temperature in top_cities.items():
        print(f"{city}: {temperature}°C")

if __name__ == "__main__":
    main()