# https://api.vk.com/method/users.get?user_ids=53656294&v=5.8&fields=nickname,status,online,country

import urllib.request
import json

def url1()
  html = urllib.request.urlopen("http://bit.ly/2Cu0ru5").read()
  data = json.loads(html)
  u = data.get('response')

  for user in u:
    print("First name: " + str(user['first_name']))
    print("Last name: " + str(user['last_name']))
    print("Nickname: " + str(user['nickname']))
    print("Status: " + str(user['status']))
    print("Online: " + str(user['online']))
    print("Сountry: " + str(user['country']))

    print('\n')
    print('_____' * 10)
    print('\n')
    
url1()
