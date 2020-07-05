import requests
from bs4 import BeautifulSoup as bs
import lxml.etree
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"

header = {'user-agent':user_agent}

myurl = 'https://movie.douban.com/top250'

response = requests.get(myurl, headers=header)

bs_info = bs(response.text, 'html.parser')
bs_info.find_all('dd')

for tags in bs_info.find_all('dd'):
    print(tags.find_all('span', attrs={'class': 'hover-tag'})[0].text)

# selector = lxml.etree.HTML(response.text)
# film_name = selector.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]/text()')
# print(film_name)




