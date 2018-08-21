from selenium import webdriver
import requests,re,time
from urllib import  request

url = 'http://m.wuyouhui.net/gushi/yirenzhixia/262970.html'
brower = webdriver.ChromeOptions()
brower.add_argument("headless")
brower = webdriver.Chrome(chrome_options=brower)
brower.get(url)
html = brower.page_source
print(html)
# pat = re.compile(r'<td align="center"><img src="(.*?)" id="qTcms_pic"',re.S)
# if pat.search(html):
#     url_img = pat.search(html).group(1)
# else:
#     pass
# # print(url_img)
# pat = re.compile(r'/<span id="k_total" class="curPage">(.*?)<img',re.S)
# max_page = pat.search(html).group(1)
# print(max_page)
# pat = re.compile(r'"BarTit">(.*?) \(<span',re.S)
# file_name = pat.search(html).group(1)
# print(file_name)


# res = requests.get(url_img)
# for i in range(1,int(max_page)+1):
#     with open(str(int(time.time()))+'.jpg','wb') as f:
#         f.write(res.content)
# request.urlretrieve(res,str(int(time.time()))+'.jpg')