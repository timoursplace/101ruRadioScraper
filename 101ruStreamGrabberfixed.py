import requests
from pathlib import Path
apilink = 'https://101.ru/api/channel/getListServersChannel/'
directory = Path('D:\download')
file = open((directory/'101ruLIST.txt'), 'a', encoding='utf8')
for number in range(1, 500):
    try:
        exept = False
        newlink = apilink + '/' + str(number)
        request = requests.get(newlink).json()
        title = request['result'][0]['titleChannel']
        url = request['result'][0]['urlStream']
        print(number)
    except:
        print(f'Could not get link for {title}')
        exept = True
    if not exept:
        file.write('Channel: ' + title + '\nLink: ' + url + '\n')
file.close()
