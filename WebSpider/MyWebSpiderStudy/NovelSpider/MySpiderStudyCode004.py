import requests
import re
#
url = 'http://www.verydm.com/'
HEADERS = {'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}



def download(url):
    dw_response = requests.get(url,headers = HEADERS)
    dw_response.encoding = dw_response.apparent_encoding
    dw_html = dw_response.text
    dw_dl = re.findall(r'<div class="chapter-type">单行本</div>(.*?)</div>',dw_html,re.S)[0]
    dw_info_list = re.findall(r'<a href="(.*?)" target=\'_blank\' title="(.*?)">',dw_dl)
    for dw_info in dw_info_list:
        dw_url,dw_title = dw_info
        print(dw_url,dw_title)

response = requests.get(url,headers = HEADERS)
response.encoding = response.apparent_encoding
html = response.text
dl = re.findall(r'<div class="head"><h3>热门</h3></div>(.*?)</div>',html,re.S)[0]
cantoon_info_list = re.findall(r'<a href="(.*?)">(.*?)<',dl)
for cantoon_info in cantoon_info_list:
    cantoon_url = cantoon_info[0]
    cantoon_title = cantoon_info[1]
    try:
        print(cantoon_title)
        download(cantoon_url)
    except BaseException:
        print('下载失败！')
        continue