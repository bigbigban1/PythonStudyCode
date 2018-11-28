import requests
import re
import os

def download(url):
    #访问传过来的url
    response = requests.get(url)
    #解码
    response.encoding = response.apparent_encoding
    #获取url的所有源码
    html = response.text
    #获取书名
    title = re.findall(r'<meta property="og:novel:book_name" content="(.*?)"/>',html)[0]
    #新建txt，保存小说
    fp = open('%s.txt'%title,'w',encoding='utf-8')
    #写入书名
    fp.write(title)
    fp.write('\n')
    #使用正则获取每一章的信息
    dl = re.findall(r'<div id="list">.*?</div>',html,re.S)[0]
    #使用正则获取url和小说名字
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
        if flag == 10:
            break
        flag+=1
