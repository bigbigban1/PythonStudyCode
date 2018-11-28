import requests
import re
import os
from bs4 import BeautifulSoup
def download(url,headers):
    fp = open('movie.txt','w',encoding='utf-8')
    response = requests.get(url,headers = headers)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text,'lxml')
    url_list = soup.find_all(name='td',attrs={'bgcolor':'#ffffbb'})
    for url in url_list:
        stR = url.decode_contents()
        url_title = re.findall(r'(.*?)：<',stR,re.S)[0]
        url_url = re.findall(r'<a href="(.*?)"',stR,re.S)[0]
        url_pwd = re.findall(r'</a> 提取码：(.*)',stR)
        if len(url_pwd) != 0:
            fp.write('%s：%s 提取码：%s\n'%(url_title,url_url,url_pwd[0]))
        else:
            fp.write('%s：%s\n' % (url_title, url_url))