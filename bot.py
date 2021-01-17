import requests
import misc
import psutil
import csv
from yobit import get_btc
from Weather import get_weather
from Vk import get_online
from Vk import clear_list
from pprint import pprint
from time import sleep
from flask import Flask
from flask import request
from flask import jsonify
from flask_sslify import SSLify
from ip import get_Location




global last_update_id
last_update_id = 0

token = misc.token

#https://api.telegram.org/bot682659449:AAGGSsk0LBFPEAEQ8ezb2IX748-NRg3MPmE/sendmessage?chat_id=485225041&text=seferg
URL = 'https://api.telegram.org/bot' + token + '/'

def get_updates(offset=200):
    url = URL + 'getupdates?offset=' + str(offset)
    r = requests.get(url)
    return r.json()



def write_json(data, filename = 'answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_message():

    while True:
        data = get_updates()
        last_object = data['result'][-1]
        update_id = last_object['update_id']

        global last_update_id
        if last_update_id != update_id:
            try:
                last_update_id = update_id
                huesos_id = data['result'][-1]['message']['chat']['id']
                chat_message = data['result'][-1]['message']['text']
                message = {'chat_id': huesos_id,
                           'message_text': chat_message}

            except KeyError:
                chat_id = huesos_id
                send_message(chat_id, text='Я не люблю картинки, я дурак я в танке горел')
                return None

            else:
                return message

        return None




def send_message(chat_id, text='Чо ты несешь, хуесос?'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)




miscfile = 'misc.py'

def main():

    print('Опять работа')
    while True:
        answer = get_message()
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['message_text']
            if 'Привет' in text:
                send_message(chat_id, 'Unte non perfecto!')
            if 'btc' in text:
                send_message(chat_id, get_btc())
            if 'weather' in text:
                send_message(chat_id, get_weather())
            if 'friends' in text:
                try:
                    send_message(chat_id, get_online())
                    clear_list()
                except:
                    TypeError
                    print('токен сломался')
                    send_message(chat_id, 'вы не указали id приложения')

        else:
            continue


if __name__ == '__main__':
    main()
    #app.run()