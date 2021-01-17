import requests
import csv
import codecs
from bs4 import BeautifulSoup
from pprint import pprint


URL = 'https://www.tvzavr.ru/novinki/'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36', 'accept': '*/*'}
titles = []
HOST = 'https://www.tvzavr.ru/novinki'


def get_html(url, params=None):
	r = requests.get(URL, headers = HEADERS, params=params)
	return r



def get_content(html):

	soup = BeautifulSoup(html, 'html.parser')
	items = soup.find_all('a', class_='card card_clip')
	for item in items:
		titles.append({
			'link': HOST + item.find('a').get_text('href'),
			'title': item.find('div', class_='card__title').get_text()
			})
	return titles


def parse():

	html = get_html(URL)
	if html.status_code == 200:
		get_content(html.text)
		pprint(titles)
	else:
		print('error')

def clear_list():
    titles.clear()

parse()