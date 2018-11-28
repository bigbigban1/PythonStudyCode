#我的第一个完整爬虫代码，参考了B站的视频https://www.bilibili.com/video/av19954075?from=search&seid=15783698962418688879
#很适合爬取小说网站，接下来我想写一个针对这个网站的综合性爬虫，能够爬取多本小说

import requests
import re

url = 'http://www.biquge.com.tw/18_18186/'
clean_dict = {' ':'','&nbsp;':'','<br />':'','<br/>':'','<divid="content">': '','</div>':''}
response = requests.get(url)
response.encoding = 'GBK'
html = response.text
title = re.findall(r'<meta property="og:novel:book_name" content="(.*?)"/>',html)[0]
fp = open('%s.txt'%title,'w',encoding='utf-8')
fp.write(title)
fp.write('\n')
dl = re.findall(r'<div id="list">.*?</div>',html,re.S)[0]
chapter_info_list = re.findall(r'<a href="(.*?)">(.*?)<',dl)
flag = 1

for chapter_info in chapter_info_list:
    chapter_url,chapter_title = chapter_info
    chapter_url = 'http://www.biquge.com.tw/%s'%chapter_url
    chapter_response = requests.get(chapter_url)
    chapter_response.encoding = 'GBK'
    chapter_html = chapter_response.text
    chapter_content = re.findall(r'</script></td><td><script>read_1_3\(\);</script></td></tr></table>(.*?)<script>read3\(\);</script><script>bdshare\(\);</script>',chapter_html,re.S)[0]
    chapter_content = chapter_content.replace(' ','')
    chapter_content = chapter_content.replace('&nbsp;','')
    chapter_content = chapter_content.replace('<br />','')
    chapter_content = chapter_content.replace('<br/>', '')
    chapter_content = chapter_content.replace('<divid="content">', '')
    chapter_content = chapter_content.replace('</div>', '')
    fp.write(chapter_title)
    fp.write(chapter_content)
    fp.write('\n')
    print('正在下载第%d章'%flag)
    flag+=1

