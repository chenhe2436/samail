import requests,json,re,os
from urllib import request
# 该程序在运行时出现以下错误
'''
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='main.gslb.ku6.com', port=80): Max retries exceeded with url: /s0/MTS_gWm_rW-TsiLhAanxvg../1473926661388/3629878ab7465c74ea71fa27129f143f/1473930136377/v445/86/84/98fef6ae4266f765a526f6b1e7b96fbf-f4v-h264-aac-626-32-294753.0-24515268-1473925792714-b2a08edf2bffea716427defdbec0c8e1-1-00-00-00.f4v?stype=mp4,http://main.gslb.ku6.com/s1/MTS_gWm_rW-TsiLhAanxvg../1473926661388/caca3aa4d1a5146c00fde2e8e7cbfc5c/1473930136377/v445/73/91/b2846c48978a2cb0b7b33493efc77e1d-f4v-h264-aac-629-32-163793.0-13669389-1473925793620-a6ca0c850bc2104ce6e68f7a9c86c7b2-2-00-00-00.f4v?stype=mp4 (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x0000000003729320>: Failed to establish a new connection: [Errno 11004] getaddrinfo failed',))
'''
page_num = 20
for i in range(5):
    headers = {
    'accept-language':'zh-CN,zh;q=0.9',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    }
    url = 'https://www.toutiao.com/search_content/?offset={}&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&cur_tab=1&from=search_tab'.format(page_num)
    html = requests.get(url)
    data = html.json()['data']
    for i in data:
        if 'article_url' in i:
            true_url = i['article_url']
            print(true_url)
            html = requests.get(true_url,headers = headers)
            html.encoding = html.apparent_encoding
            data_str = html.text
            pat = re.compile(r'title: \'(.*)\'')
            res = pat.search(data_str)
            if res:
                title = res.group(1)
            else:
                continue
            if not os.path.exists(title):
                os.makedirs(title)
            pat = re.compile(r'gallery: JSON.parse\((.*)\),')
            data_sear = pat.search(data_str)
            if data_sear:
                data_sear = data_sear.group(1)
                data_str = json.loads(data_sear)
            else:
                os.removedirs(title)
                continue
            data = json.loads(data_str)
            for img in data['sub_images']:
                url = img['url'] # http://p1.pstatp.com/origin/pgc-image/1534382713538b7b414b730
                name = url.split('/')[-1] + '.jpg'
                request.urlretrieve(url,title + '/' + name)
                print(title + '/' + name)
    page_num += 20
