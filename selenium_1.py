from selenium import webdriver
import time
import requests
from lxml import etree
import base64

# https://market.aliyun.com/products/57124001/cmapi028447.html?spm=5176.2020520132.101.5.zdlUnT#sku=yuncode2244700000
# 操作浏览器
driver = webdriver.Chrome()
url = 'https://accounts.douban.com/login?alias=&redir=https%3A%2F%2Fwww.douban.com%2F&source=index_nav&error=1001'

driver.get(url)
time.sleep(1)
driver.find_element_by_id('email').send_keys('18510556963')
time.sleep(1)
driver.find_element_by_id('password').send_keys('')
time.sleep(1)

# 获取验证码相关信息
html_str = driver.page_source
html_ele = etree.HTML(html_str)
# 得到验证码的url
image_url = html_ele.xpath('//img[@id="captcha_image"]/@src')[0]
# 获取这个图片的内容
response = requests.get(image_url)

# 获取base64的str
#  https://market.aliyun.com/products/57124001/cmapi028447.html?spm=5176.2020520132.101.5.2HEXEG#sku=yuncode2244700000
b64_str = base64.b64encode(response.content)
v_type = 'cn'
# post 提交打码平台的数据
form = {
    'v_pic': b64_str,
    'v_type': v_type,
}

# authtication的header
headers = {
    'Authorization': 'APPCODE eab23fa1d03f40d48b43c826c57bd284',
}
# 从打码平台获取验证码信息
dmpt_url = 'http://yzmplus.market.alicloudapi.com/fzyzm'
response = requests.post(dmpt_url, form, headers=headers)
print(response.text)
# captcha_value 就是我们的验证码信息
captcha_value = response.json()['v_code']

print(image_url)
print(captcha_value)
# captcha_value = input('请输入验证码')

driver.find_element_by_id('captcha_field').send_keys(captcha_value)
time.sleep(1)
driver.find_element_by_class_name('btn-submit').click()
time.sleep(1)
# 获取所有的cookie的信息
cookies = driver.get_cookies()
cookie_list =[]

# 对于每一个cookie_dict, 就是将name 和 value取出, 拼接成name=value;
for cookie_dict in cookies:
    cookie_str = cookie_dict['name'] + '=' + cookie_dict['value']
    cookie_list.append(cookie_str)

# 拼接所有的cookie到header_cookie中
header_cookie = '; '.join(cookie_list)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Cookie': header_cookie,
}
another_url = 'https://www.douban.com/accounts/'
response = requests.get(another_url, headers=headers)

with open('cc.html', 'wb') as f:
    f.write(response.content)


# with open('douban.html', 'wb') as f:
#     f.write(driver.page_source.encode('utf-8'))

