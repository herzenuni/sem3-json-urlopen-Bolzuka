# https://api.vk.com/method/users.get?user_ids=53656294&v=5.8&fields=nickname,status,online,country

import requests
import urllib.request
import json

def url_constractor(*args):
    html = 'https://api.vk.com/method/users.get?user_ids='
    for item in args:
        html += str(item) + ','
    html = html[0:-1]
    html += '&v=5.8&fields=nickname,status,online,country'
    return html

def main():
    ids = [53656294]
    try:
      html = urllib.request.urlopen(url_constractor(*ids)).read()
    except requests.exceptions.HTTPError as e:
        print('>>{}!'.format(e)) 
    except requests.exceptions.ConnectionError as e:
        print('>>{}!'.format(e)) 
    else:

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

            
if __name__ == '__main__':
   main()
