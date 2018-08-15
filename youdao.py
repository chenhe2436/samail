def trans(kw):
    import imp,time,hashlib,random,json
    pachong = imp.load_source('aaa', 'E:\\kecheng\\richang\\Py10_2018_08_13\\day1\\tuozhan_all.py')
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '214',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'P_INFO=m13269416588@163.com|1533294086|0|other|00&99|anh&1533046043&other#anh&340100#10#0#0|132588&1|ecard&urs&mailuni|13269416588@163.com; OUTFOX_SEARCH_USER_ID=328758464@10.169.0.83; JSESSIONID=aaaQobwLpgTY07Vkvw2uw; OUTFOX_SEARCH_USER_ID_NCOO=685455434.6356416; ___rl__test__cookies=1534217058511',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    salt = str(int(time.time()*1000))
    S = "fanyideskweb"
    r = salt
    D = "ebSeFb%=XZ%T[KZ)c(sy!"
    md = hashlib.md5()
    md.update((S+kw+r+D).encode(encoding='utf-8'))
    sign = md.hexdigest()
    data = {
        'i':kw,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':salt,
        'sign':sign,
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTIME',
        'typoResult':'false',
    }
    res = json.loads(pachong.post(url,data,headers).decode('utf-8'))
    return (kw+'的翻译结果为：'+res["translateResult"][0][0]['tgt'])

if __name__ == '__main__':
    while 1:
        kw = input('请输入要翻译的内容：')
        res = trans(kw)
        print(res)