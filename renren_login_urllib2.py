from tuozhan_all import opener,post,get,res
import json
# url
url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018721441132'
# form
form = {
    'email': '18555111271',
    'icode': '',
    'origURL:http': '//www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'password': '48ad96ce5a49e2ef9eb8077a71a6e82a42852dff75c726c167eaf7718f3ed7c1',
    'rkey': 'c3fe0fee33045b75e4b4af194b111c69',
    'f': 'http%3A%2F%2Fwww.renren.com%2F967453953%2Fprofile',
}
opener = opener()
req = post(url, form, opener=opener)
opener,html_bytes = res(req, opener)
#html_bytes = post(url, form=form)
# 打印结果
#print(html_bytes)
# 通过json获取一个字典类型
res_dict = json.loads(html_bytes.decode('utf-8'))
home_url = res_dict['homeUrl']
# 访问页面
req = get(home_url)
opener,html_bytes = res(req, opener)
print(html_bytes.decode('utf-8'))
with open('renren.html','wb') as f:
    f.write(html_bytes)

