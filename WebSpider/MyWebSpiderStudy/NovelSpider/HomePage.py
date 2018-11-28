import requests
import re
import os
from Download import download
url = 'http://www.biquge.com.tw/xiuzhen/'

os.mkdir('G:\\pycode\\novel')
os.chdir('G:\\pycode\\novel')
 #访问url
home_response = requests.get(url)
#解码
home_response.encoding = home_response.apparent_encoding
#获取url的所有内容
home_html = home_response.text
#使用正则表达式获取最新的内容
home_new = re.findall(r'<div class="r">(.*?)<div class="clear">',home_html,re.S)[0]
#使用正则表达式提取url，书名，作者
home_info_list = re.findall(r'<a href="(.*?)">(.*?)</a></span><span class="s5">(.*?)<',home_new)
for home_info in home_info_list:
    novel_url = home_info[0]
    novel_name = home_info[1]
    novel_author = home_info[2]
    print('正在下载%s写的《%s》'%(novel_author,novel_name))
    download(novel_url)