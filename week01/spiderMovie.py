import requests

from bs4 import BeautifulSoup as bs


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"

accept_Encoding = 'gzip, deflate, br'
Accept_Language = 'zh-CN,zh;q=0.9,en;q=0.8'
Host = 'catfront.dianping.com'
Origin = 'https://maoyan.com'

header = {'user-agent':user_agent, 'Accept-Encoding': 'gzip, deflate, br',
          'Accept-Language':Accept_Language,
          'Host': 'monitor.maoyan.com', 'Origin':'https://maoyan.com',
          'Referer': 'https://maoyan.com/films?showType=3',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          'Host': 'maoyan.com',
          'Upgrade-Insecure-Requests': '1'
          }

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl, headers=header)

bs_info = bs(response.text, 'html.parser')
list = bs_info.find_all('div', attrs={'class', 'movie-item film-channel'})
for i in range(len(list)):
    for tag in list[i].find_all('div', attrs={'class': 'movie-hover-info'}):
        print(tag.find_all('div')[0].find('span', attrs={'class', 'name'}).text)
        print(tag.find_all('div')[1].text.replace('类型:', '').replace(' ', ''))
        print('----------')

    if i==9:
        break