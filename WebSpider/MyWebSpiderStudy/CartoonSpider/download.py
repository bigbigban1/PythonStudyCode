import requests
import re
import time
import urllib.request

HEADERS = {'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
REFER = 'http://www.verydm.com'

def download(url,path):
    time.sleep(10)
    response = requests.get(url,headers = HEADERS)
    response.encoding = 'utf-8'
    html = response.text
    html_picture = re.findall(r'<div class="main"  style="display:block">(.*?)</div>',html,re.S)[0]
    html_picture_url = re.findall('<img src="(.*?)" id',html_picture)[0]
    urllib.request.urlretrieve(html_picture_url,path)