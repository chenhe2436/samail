from lxml import etree
import requests, re, os
from urllib import request

url = 'https://www.ximalaya.com/revision/play/album?albumId=4164479&pageNum=1&sort=-1&pageSize=30'

# https://www.ximalaya.com/revision/play/album?albumId=4164479&pageNum=1&sort=-1&pageSize=30
#
headers = {
'Accept':'*/*',
# 'Accept-Encoding':'gzip, deflate, br',
# 'Accept-Language':'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
'Cookie':'Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070=1534474961,1534477578; Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070=1534477578',
'Host':'www.ximalaya.com',
'Referer':'https://www.ximalaya.com/lishi/4164479/',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
}
html = requests.get(url, headers=headers)
response_str = html.text
pat = re.compile(r'"src":"(.*?)"',re.S)
url_list = pat.findall(response_str)
if not os.path.exists('喜马拉雅_春秋'):
    os.makedirs('喜马拉雅_春秋')
for url in url_list:
    name = url.split('/')[-1]
    print('正在下载：'+ url)
    filename = '喜马拉雅_春秋/' + name
    request.urlretrieve(url,filename)

 