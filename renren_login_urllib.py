from tuozhan_all import session
import json
# url
url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018721441132'
# form
form = {
    'email': '18510556963',
    'icode': '',
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'password': '95cb2a1d59b918e0d16ab5d3535fb40103e4b546e651a3e3c99b91876927c78a',
    'rkey': 'a7bccfbafd7ee702247450942dff5611',
    'f': 'http%3A%2F%2Fwww.renren.com%2F966927992',
}

s = session()
html_bytes = s.post(url, form)

#html_bytes = post(url, form=form)
# 打印结果
#print(html_bytes)
# 通过json获取一个字典类型
res_dict = json.loads(html_bytes.decode('utf-8'))

home_url = res_dict['homeUrl']

# 访问页面
html_bytes = s.get(home_url)
print(html_bytes.decode('utf-8'))

