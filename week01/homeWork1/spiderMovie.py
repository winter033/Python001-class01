import requests

from bs4 import BeautifulSoup as bs
import pandas as pd


accept_Encoding = 'gzip, deflate, br'
Accept_Language = 'zh-CN,zh;q=0.9,en;q=0.8'
Host = 'catfront.dianping.com'
Origin = 'https://maoyan.com'
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Host': 'monitor.maoyan.com', 'Origin': 'https://maoyan.com',
    'Referer': 'https://maoyan.com/films?showType=3',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Host': 'maoyan.com',
    'Upgrade-Insecure-Requests': '1',
    'Cookie': 'uuid_n_v=v1; uuid=C8FBFB90B6E311EA8A833903D31672832D31C1A56A9F4F2BBB988B8A11ADD6FD; mojo-uuid=4f04fa1b718dfffdafc49edecd7742e1; _lxsdk_cuid=172eb905bd3c8-0d15d482ca3a6c-f7d123e-1fa400-172eb905bd4c8; _lxsdk=C8FBFB90B6E311EA8A833903D31672832D31C1A56A9F4F2BBB988B8A11ADD6FD; _csrf=cdadbefb522ecc4c2bd08550f57208dfff3665e47133b1913d488e4c2bcf913b; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593160973,1593162052,1593270450,1593348222; mojo-session-id={"id":"f345c562a9577f0b35ad8a078fe0330b","time":1593352443533}; mojo-trace-id=2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593352490; __mta=252475062.1593090006078.1593352443768.1593352489744.18; _lxsdk_s=172fb34d2a4-97c-485-0fa%7C%7C5'
}
myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl, headers=header)
name = ['名称', '类型', '时间']
movie = []
bs_info = bs(response.text, 'html.parser')
list = bs_info.find_all('div', attrs={'class', 'movie-item film-channel'})
for i in range(10):
    for tag in list[i].find_all('div', attrs={'class': 'movie-hover-info'}):
        movie_name = tag.find_all('div')[0].find('span', attrs={'class', 'name'}).text
        movie_type = tag.find_all('div')[1].text.replace('类型:', '').replace(' ', '')
        movie_time = tag.find_all('div')[3].text.replace('上映时间:', '').replace(' ', '')
        movie.append([movie_name, movie_type, movie_time])
        print('----------')

pd.DataFrame(columns=name, data=movie).to_csv('movie.csv', encoding='utf-8')