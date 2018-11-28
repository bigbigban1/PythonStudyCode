#吴世龙给我改进的

import re

import requests

url = 'http://www.biquge.com.tw/14_14055/'
clean = [' ','&nbsp;','<br />','<br/>','<divid="content">','</div>']
response = requests.get(url)
response.encoding = 'GBK'
html = response.text
title = re.findall(r'<meta property="og:novel:book_name" content="(.*?)"/>',html)[0]
fp = open('%s.txt'%title,'w',encoding='utf-8')
fp.write('title')
fp.write('\n')
dl = re.findall(r'<div id="list">.*?</div>',html,re.S)[0]
chapter_info_list = re.findall(r'<a href="(.*?)">(.*?)<',dl)
flag = 1

rep_dct = {'&nbsp;':' ','<br />':'','\r\n\r\n':'\n'}
def filters(match):
    rep_s = match.group(2)
    for k,v in rep_dct.items():
        rep_s = rep_s.replace(k,v)
    return rep_s


for chapter_info in chapter_info_list:
    chapter_url,chapter_title = chapter_info
    chapter_url = 'http://www.biquge.com.tw/%s'%chapter_url
    chapter_response = requests.get(chapter_url)
    chapter_response.encoding = chapter_response.apparent_encoding
    chapter_html = chapter_response.text
    chapter_content = re.sub(r'(.*</script></td><td><script>read_1_3\(\);</script></td></tr></table>.*<div id="content">(.*?)</div>.*<script>read3\(\);</script><script>bdshare\(\);</script>.*)',filters,chapter_html,flags=re.S)
    fp.write(chapter_title)
    fp.write(chapter_content)
    fp.write('\n')
    print('正在下载第%d章'%flag)
    flag+=1

def out():
    print(1)