import requests
import re
import os
from bs4 import BeautifulSoup

url = 'https://www.3dmgame.com/'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
#设置新闻文件保存的路径
dir = 'G:\\pycode\\WebSpider\\MyWebSpiderStudy\\ArticleSpider'
try:
    os.chdir(dir)
except BaseException:
    print("目录不存在！请更改目录或创建目录")
fp = open('news.txt','w',encoding='utf-8')
#发起访问请求
response = requests.get(url,headers = headers)
#解码
response.encoding = response.apparent_encoding
#调用BS4
soup = BeautifulSoup(response.text,'html.parser')
#找到新闻所在的div
div = soup.find(name='div',attrs={'style':'display: block'})
#找到新闻所在的li
li_list = div.find_all(name = 'li')
article_url_list = []
for li in li_list:
    #找到新闻中包含url的a标签
    article_info = li.find(name = 'a')
    #这里是使用正则剥离新闻标题
    # article_title = re.findall(r'<a.*?>(.*?)</a>',li.decode_contents(),re.S)[0]
    # print(article_title)
    #剥离出url，将其加入到列表中
    article_url_list.append(article_info.attrs.get('href'))
#为了减少时间复杂度，不采用for循环嵌套，实际上这部分写在上面的for循环里面也是可以的
for article_url in article_url_list:
    #访问每篇新闻的url
    article_response = requests.get(article_url ,headers = headers)
    #解码
    article_response.encoding = article_response.apparent_encoding
    #调用BS4
    article_soup = BeautifulSoup(article_response.text,'html.parser')
    #剥离出新闻的标题
    div = article_soup.find(name='div',attrs={'class':' news_warp_top'})
    try:
        article_title = div.find(name = 'h1')
    except BaseException:
        continue
    fp.write(article_title.text)
    print("正在爬取文章：%s"%article_title.text)
    fp.write('\n')
    #获取文章来源
    if article_soup.find(name='span',attrs={'class':'weibo'}) != None:
        article_source = article_soup.find(name='span',attrs={'class':'weibo'}).text
        fp.write('来源：%s\t'%article_source)
    #获取文章作者
    if article_soup.find(name='span',attrs={'class':'name'}) != None:
        article_author = article_soup.find(name='span',attrs={'class':'name'}).text
        fp.write('作者：%s\t' % article_author)
    #获取文章编辑
    if article_soup.find(name='span',attrs={'class':'bianji'}) != None:
        article_editor = article_soup.find(name='span',attrs={'class':'bianji'}).text
        fp.write('编辑：%s\n' % article_editor)
    #这里开始不使用Beautifulsoup了，因为我也不知道为什么找不到文章所在的div，报错来着，于是使用正则
    article_html = article_response.text
    #使用正则匹配文章段落所在的div
    article_pragh_dl = re.findall(r'<div class="news_warp_center">(.*?)</div>',article_html,re.S)[0]
    #使用正则匹配每一段文章
    article_pragh_list = re.findall(r'<p style="text-indent:2em;">(.*?)</p>',article_pragh_dl,re.S)
    for article_pragh in article_pragh_list:
        #清洗文章，还有一个问题就是超链接洗不掉，我还得再研究研究
        article_pragh.replace('<strong>', '')
        article_pragh.replace('</strong>', '')
        #保存文章内容，格式很不好看，还得再学习
        fp.write(article_pragh)
    fp.write('*****************************************************************************************\n')