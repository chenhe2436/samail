import requests,re,pymysql,time
from multiprocessing import Process,Pool,Queue


def paqu(q):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }
    for i in range(1, 101):
        url = 'http://www.xicidaili.com/nn/{}'.format(i)
        html = requests.get(url, headers=headers)
        data = html.text
        pat = re.compile(r'\<td\>(\d{1}\S+\d+?)\<\/td\>.*?<td>(\d+?)</td>', re.S)
        ur = pat.findall(data)
        q.put(ur)

def shaixuan(sql,ip_tuple):
    url = 'http://www.baidu.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }
    print(123)
    try:
        proxy = {
            'http': 'http://%s:%s' % (ip_tuple[0], ip_tuple[1]),
            'https': 'http://%s:%s' % (ip_tuple[0], ip_tuple[1]),
        }
        html = requests.get(url, headers=headers, proxies=proxy, timeout=3)
        if html:
            cursor.execute(sql, ip_tuple)
            db.commit()
    except:
        print('该代理请求超时',ip_tuple[0])


if __name__ == '__main__':
    db = pymysql.connect('127.0.0.1', 'root', 'chenhe', 'pachong')
    cursor = db.cursor()
    sql = 'insert into url_true(ip,port) VALUES (%s,%s)'
    q = Queue()
    p = Process(target=paqu,args=(q,))\i
    p.start()
    time.sleep(5)
    if not q.empty():
        pool = Pool(5)
        while 1:
            try:
                if q.qsize() != 0:
                    ip_tuple = q.get()
                    print(ip_tuple)
                    pool.apply_async(shaixuan,(sql,ip_tuple))
                else:
                    break
            except:
                continue
        cursor.close()
        db.close()


