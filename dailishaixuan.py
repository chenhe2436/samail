# 筛选100页西刺代理当中的优质代理
import requests,re,threading,pymysql
db = pymysql.connect('127.0.0.1','root','chenhe','pachong')
cursor = db.cursor()
sql = 'insert into url_true(ip,port) VALUES (%s,%s)'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}
iplist = []
# 100页IP爬取并存储
for i in range(1, 101):
    url = 'http://www.xicidaili.com/nn/{}'.format(i)
    html = requests.get(url,headers=headers)
    data = html.text
    pat = re.compile(r'\<td\>(\d{1}\S+\d+?)\<\/td\>.*?<td>(\d+?)</td>', re.S)
    ur = pat.findall(data)
    iplist.append(ur)
for ur_list in iplist:
    for ip_tuple in ur_list:
        url = 'http://www.baidu.com'
        try:
            proxy = {
                'http': 'http://%s:%s' % (ip_tuple[0], ip_tuple[1]),
                'https': 'http://%s:%s' % (ip_tuple[0], ip_tuple[1]),
            }
            html = requests.get(url, headers=headers, proxies=proxy ,timeout=3)
            print(str(ip_tuple)+'该IP可用，正在存储到MySQL')
            cursor.execute(sql,ip_tuple)
            db.commit()
            print('储存完毕')
        except:
            print('请求超时，更换代理继续中……')
            continue
cursor.close()
db.close()
print('测试完毕，请检查数据库！')