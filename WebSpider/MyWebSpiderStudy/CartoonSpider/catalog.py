import requests
import re
import os
from download import download

HEADERS = {'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
REFER = 'http://www.verydm.com'
def catalog(url):
    response = requests.get(url,headers = HEADERS)
    response.encoding = 'utf-8'
    html = response.text
    title = re.findall(r'<meta name="keywords" content="(.*?)">',html,re.S)[0]
    try:
        os.mkdir('G:\\pycode\\WebSpider\\MyWebSpiderStudy\\CartoonSpider\\%s'%title)
        print('文件夹创建成功！')
    except BaseException:
        print('文件夹已存在，不再建立！')
    os.chdir('G:\\pycode\\WebSpider\\MyWebSpiderStudy\\CartoonSpider\\%s'%title)
    catalog_dl = re.findall(r'<div class="chapters">(.*?)<div class="related">',html,re.S)[0]
    catalog_type = re.findall(r'<div class="chapter-type">(.*?)</div>',catalog_dl)
    for catalog_type_one in catalog_type:
        print('正在下载%s'%catalog_type_one)
        try:
            os.mkdir('G:\\pycode\\WebSpider\\MyWebSpiderStudy\\CartoonSpider\\%s\\%s' %(title,catalog_type_one))
            print('分卷文件夹创建成功！')
        except BaseException:
            print('分卷文件夹已存在，不再建立！')
        os.chdir('G:\\pycode\\WebSpider\\MyWebSpiderStudy\\CartoonSpider\\%s\\%s' % (title, catalog_type_one))
        catalog_type_dl = re.findall(r'<div class="chapter-type">%s</div>(.*?)</ul>'%catalog_type_one,catalog_dl,re.S)[0]
        catalog_type_info = re.findall(r'<a href="(.*?)" target=\'_blank\' title="(.*?)">',catalog_type_dl)
        flag = 1
        for catalog_type_info_one in catalog_type_info:
            catalog_type_url = catalog_type_info_one[0]
            catalog_type_title = catalog_type_info_one[1]
            print('正在下载%s'%catalog_type_title)
            try:
                os.mkdir('G:\\pycode\\WebSpider\\MyWebSpiderStudy\\CartoonSpider\\%s\\%s\\%s' % (title,catalog_type_one, catalog_type_title))
                print('漫画文件夹创建成功！')
            except BaseException:
                print('漫画文件夹已存在，不再创建！')
            os.chdir('G:\\pycode\\WebSpider\\MyWebSpiderStudy\\CartoonSpider\\%s\\%s\\%s' % (title,catalog_type_one, catalog_type_title))
            download_url = 'http://www.verydm.com%s&p=1'%catalog_type_url
            path = 'G:\\pycode\\WebSpider\\MyWebSpiderStudy\\CartoonSpider\\%s\\%s\\%s' % (title,catalog_type_one, catalog_type_title)
            download(download_url,path)
catalog('http://www.verydm.com/manhua/aiyuyuwang')