from urllib import request, parse
from urllib.error import HTTPError, URLError
# 保存cookie
from http import cookiejar

class session(object):
    def __init__(self):
        cookie_object = cookiejar.CookieJar()
        # handler 对应着一个操作
        handler = request.HTTPCookieProcessor(cookie_object)
        # opener 遇到有cookie的response的时候,
        # 调用handler内部的一个函数, 存储到cookie object
        self.opener = request.build_opener(handler)

    def get(self, url, headers=None):
        return get(url, headers, self.opener)

    def post(self, url, form, headers=None):
        return post(url, form, headers, self.opener)

#a. get(url, headers=None)

def get(url, headers=None, opener = None):
    return urlrequests(url, headers=headers, opener = opener)

def post(url, form, headers=None, opener = None):
    return urlrequests(url, form, headers=headers, opener=opener)

#b. post(url, form, headers=None)

#1. 传入url
#2. user_agent
#3. headers
#4. 定义Request
#5. urlopen
#6. 返回byte数组
def urlrequests(url, form=None, headers=None, opener = None):

    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    # 如果用户需要自行传入headers, 则覆盖之前的headers
    if headers == None:
        headers = {
            'User-Agent': user_agent
        }
    html_bytes = b''
    try:
        if form:
            # POST
            # 2.1 转换成str
            form_str = parse.urlencode(form, encoding='utf-8')
            #print(form_str)
            # 2.2 转换成bytes
            form_bytes = form_str.encode('utf-8')
            req = request.Request(url, data=form_bytes, headers=headers)
        else:
            # GET
            req = request.Request(url, headers=headers)
        if opener:
            response = opener.open(req)
        else:
            response = request.urlopen(req)
        html_bytes = response.read()
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)

    return html_bytes

if __name__ == '__main__':
    # url = 'http://fanyi.baidu.com/sug'
    # form = {
    #     'kw': '呵呵'
    # }
    # html_bytes = post(url, form=form)
    # print(html_bytes)

    url = 'http://www.baidu.com'
    html_byte = get(url)
    print(html_byte)
