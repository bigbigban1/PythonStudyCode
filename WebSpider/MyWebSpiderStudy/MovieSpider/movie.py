import requests
import re
from dw_movie import download
from bs4 import BeautifulSoup

url = 'http://www.dygang.net/ys/index.htm'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
response = requests.get(url,headers = headers)
response.encoding = response.apparent_encoding

soup = BeautifulSoup(response.text,'lxml')
tb_list = soup.find_all(name='table',attrs={'width':'388'})
fp = open('movie.txt','w',encoding='utf-8')
for tb in tb_list:
    url_info = tb.find(name='a',attrs={'class':'classlinkclass'})
    url = url_info.get('href')
    title = url_info.decode_contents()
    fp.write('%s\n'%title)
    print('正在爬取%s的信息'%title)
    try:
        download(url,headers)
    except BaseException:
        continue
