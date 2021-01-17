import requests
import misc
from pprint import pprint

access_token = misc.access_token
friends_name = []

def get_online():
    online = 'https://api.vk.com/method/friends.getOnline?&fields=bdate&access_token=' + access_token + '&v=5.85'
    fr = requests.get(online).json()
    num_online = len(fr['response'])
    for i in fr:
        for b in range(num_online):
            Z = ('https://api.vk.com/method/users.get?user_ids={}&fields=bdate&access_token={}&v=5.85').format(str(fr['response'][b]), access_token)
            z = requests.get(Z).json()
            u = z['response'][0]['first_name']
            U = z['response'][0]['last_name']
            Uu = u + ' ' + U
            friends_name.append(Uu)
            b + 1
        online = ' \n'.join(map(str, friends_name))
    return str(len(friends_name)) + ' ДРУЗЕЙ ОНЛАЙН:' + '\n' + online

def clear_list():
    friends_name.clear()



