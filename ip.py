import requests
from pprint import pprint



def get_Location():
    ip = requests.get("https://api.2ip.ua/geo.json?ip=").text
    pprint(ip)
    try:
        Location = ip['ip']
        return 'IP: ' + Location
    except TypeError:
        z = "IP: Превышено кол-во запросов"
        return z


def main():
    pprint(get_Location())

if __name__ == "__main__":
    main()