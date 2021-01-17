import requests
import telebot
import sqlite3
from time import sleep
import json


v_token = "28ca2becfa34a382fe6315d777d91979ba341eb5976ea8db5399772f59296b3d724e8999a9890723bfd7c"
tb = telebot.TeleBot("1191271331:@SusChannelPepega")
admin_id = 485225041
group_id = -1001213484493
image_group = [147754208, 80819137, 65487256, 101240674, 79496073]


def write_group_and_url_photo(group_id, photo_url):
	con = sqlite3.connect("group_and_photo.db")
	cur = con.cursor()
	cur.execute(f"""CREATE TABLE IF NOT EXISTS GAUP (group_id int, image_url text);""") 
	cur.execute(f"INSERT INTO GAUP VALUES(?,?)", (group_id, photo_url))
	con.commit()
	cur.close() 
	con.close()


def get_last_post(group_id):
	con = sqlite3.connect("group_and_photo.db")
	cur = con.cursor()	
	cur.execute(f"SELECT * FROM GAUP WHERE group_id = ?", [(group_id)])
	data = cur.fetchall()
	con.commit()
	cur.close() 
	con.close()	
	return data[-1][-1]


def vk_exec(method, param):
	URL = "https://api.vk.com/method/" + method + "?" + param
	return requests.get(URL).json()


def wall_img(group_id, offset=None):
	if offset == None:
		get_image = vk_exec("wall.get", f"owner_id=-{group_id}&v=5.35&count=1&access_token={v_token}")
	else:
		get_image = vk_exec("wall.get", f"owner_id=-{group_id}&v=5.35&offset={offset}&count=1&access_token={v_token}")
	with open('data.json', 'w') as f:
		f.write(json.dumps(get_image))
	with open('data.json', 'r', encoding='utf-8') as f:
		dat = json.load(f)
	try:
		if 'items' in dat['response']:
			if 'is_pinned' not in dat['response']['items'][0]:
				if 'attachments' in dat['response']['items'][0]:
					if 'photo' in dat['response']['items'][0]['attachments'][0] and 'album' not in dat['response']['items'][0]['attachments'][0]:
						photo = dat['response']['items'][0]['attachments'][0]['photo']['photo_604']
						return [group_id, photo]
					else:
						return 'NOIMAGE'	
				else:
					return 'NOIMAGE'
			else:
				return wall_img(image_group[0], 1)
		else:
			return 'NOIMAGE'
	except Exception as e:
		get_image = vk_exec("wall.get", f"owner_id=-{group_id}&v=5.35&count=1&access_token={v_token}")
		if get_image['error']['error_code'] == 5:
			tb.send_message(admin_id, 'Error: \n\n' + 'USER TOKEN IS BLOCKED') # если токен не валид
		elif get_image['error']['error_code'] == 6:
			tb.send_message(admin_id, 'Error: \n\n' + 'TOO MANY REQUESTS PER SECOND') # слишком много запросов в секунду
		else:
			tb.send_message(admin_id, 'Error: \n\n' + str(e))
		sleep(2)


def main():
	while True:
		for i in image_group:
			try:
				with open('d.json', 'w') as f:
					f.write(json.dumps({'img_f': wall_img(i)}))
				with open('d.json', 'r', encoding='utf-8') as f:
					dat = json.load(f)
				if type(dat['img_f']) is list:
					if dat['img_f'][-1] != get_last_post(i): 
						write_group_and_url_photo(dat['img_f'][0], dat['img_f'][-1])
						tb.send_photo(group_id, dat['img_f'][-1])
			except Exception as e:
				tb.send_message(admin_id, 'In main script error: \n\n' + str(e))
		print('Ahhhh... Again this ..')
		sleep(900)


if __name__ == '__main__':
	print('START')
	main()