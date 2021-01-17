import requests
import csv
import codecs
import sqlite3
from bs4 import BeautifulSoup
from pprint import pprint

db = sqlite3.connect('server.db')
sql = db.cursor()
URL = 'https://kwork.ru/projects?c=41'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36', 'accept': '*/*'}
FILE = 'qwe.csv'

sql.execute("""CREATE TABLE IF NOT EXISTS table1 (
	title TEXT,
	link TEXT
	)""")
db.commit()


def get_html(url, params=None):
	r = requests.get(URL, headers = HEADERS, params=params)
	return r
	
def get_content(html):
	
	soup = BeautifulSoup(html, 'html.parser')
	items = soup.find_all('div', class_='wants-card__header-title first-letter breakwords pr250')
	pprint(items)
	for item in items:
		sql.execute(f"INSERT INTO table1 VALUES (?, ?)", (item.find().get_text(strip=True), item.find().get('href')))
		db.commit()
	pass

def parse():
	html = get_html(URL)
	if html.status_code == 200:
		get_content(html.text)
		for value in sql.execute("SELECT * FROM table1"):
			print(value)
	else:
		print('error')

parse()