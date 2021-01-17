import requests
from pprint import pprint



def get_weather():
    Karagandy = 'http://api.openweathermap.org/data/2.5/weather?id=609655&appid=9f9523ace08cf398c2a5f34078856038'
    K = requests.get(Karagandy).json()
    WeatherK = K['main']['temp']
    WindK = K['wind']['speed']
    return 'Температура: ' + str(round(WeatherK - 273)) + ' ℃' + '\n' + 'Скорость ветра: ' + str(WindK) + ' М/С'

def main():
    pprint(get_weather())

if __name__ == "__main__":
    main()