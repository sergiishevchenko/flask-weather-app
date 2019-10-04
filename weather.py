import requests


def weather_by_city(city_name):
    weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    params = {
        'key': '94df97d243cc4535be7162743191409',
        'q': city_name,
        'format': 'json',
        'num_of_days': 1,
        'lang': 'ru'
    }

    try:
        result = requests.get(weather_url, params=params)
        result.raise_for_status()
        weather = result.json()
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except (IndexError, TypeError):
                    return False
    except(requests.RequestException, ValueError):
        print("Error")
        return False
    return False


if __name__ == '__main__':
    print(weather_by_city('Lausanne, Switzerland'))
