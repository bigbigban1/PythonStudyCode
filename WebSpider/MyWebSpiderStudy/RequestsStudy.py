import requests
import re

url = 'http://www.biquge.com.tw/6_6595/'
response = requests.get(url)
response.encoding = 'gbk'
html = response.text
author = re.findall(r'<meta property="og:novel:author" content="(.*?)"/>',html,re.S)[0]
name = re.findall(r'<meta property="og:novel:book_name" content="(.*?)"/>',html,re.S)[0]
div = re.findall(r'<div id="list">(.*?)</div>',html,re.S)[0]
chapter_info_list = re.findall(r'<a href="(.*?)">(.*?)<',div)
fp = open('%s.txt'%name,'w',encoding='utf-8')
fp.write('《%s》    '%name)
fp.write('%s\n'%author)
flag = 1
for chapter_info in chapter_info_list:
    chapter_url = chapter_info[0]
    chapter_title = chapter_info[1]
    chapter_url = 'http://www.biquge.com.tw%s'%chapter_url
    chapter_response = requests.get(chapter_url)
    chapter_response.encoding = 'gbk'
    chapter_div = re.findall(r'div id="content"(.*?)</div>',chapter_response.text,re.S)[0]
    chapter_article_list = re.findall(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<',chapter_div,re.S)
    print('正在爬取第%d章'%flag)
    for chapter_article in chapter_article_list:
        fp.write(chapter_article)
        fp.write('\n')
    flag += 1
