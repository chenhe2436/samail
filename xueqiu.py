from urllib import request
import json,pymysql,time,random
# 构建url
db = pymysql.connect('127.0.0.1','root','chenhe','pachong')
max_id = -1
# 构建请求头
headers = {
      'Accept': '*/*',
      # 'Accept-Encoding':'gzip, deflate, br',
      'Accept-Language': 'zh-CN,zh;q=0.9',
      'Connection': 'keep-alive',
      'Cookie': 'aliyungf_tc=AQAAAKuV62c20QUAUhVFecdTkwIXyhDf; xq_a_token=584d0cf8d5a5a9809761f2244d8d272bac729ed4; xq_a_token.sig=x0gT9jm6qnwd-ddLu66T3A8KiVA; xq_r_token=98f278457fc4e1e5eb0846e36a7296e642b8138a; xq_r_token.sig=2Uxv_DgYTcCjz7qx4j570JpNHIs; Hm_lvt_1db88642e346389874251b5a1eded6e3=1534296134; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1534296134; u=501534296134618; device_id=5821ab3d5d6d41d68866e1d3777c0855; _ga=GA1.2.1627731980.1534296140; _gid=GA1.2.1270575609.1534296140; _gat_gtag_UA_16079156_4=1',
      'Host': 'xueqiu.com',
      'Referer': 'http://xueqiu.com/',
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
      'X-Requested-With': 'XMLHttpRequest',
}
for i in range(3):
      url = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?' \
            'since_id=-1&max_id={}&count=10&category=111'.format(max_id)
      # 发起请求
      req = request.Request(url=url, headers=headers)
      html = request.urlopen(req)
      res = html.read().decode('utf-8')
      data = json.loads(res)
      print(data)
      max_id = data['next_max_id']
      # # id = data['list'][0]['data']['id'] # {"list":[{"id":184331,"category":0,
      # # "data":"{\"id\":112107004,\"title\":\"东南西北各路共产房，下一个网申的可能是她？！\",\"description\":\"今天顺义金港嘉园的审核结果出来了，不用我出手，顺义群里的同学已经自行算出了中签率： 第一组444户不通过，9156通过。房源910套。中签比10.1:1第二组237户不通过，1680通过。房源390套。中签比4.3:1 审核结果一出，就摇号
      # # 'next_max_id': 184205
      for data in data['list']:
            data = data['data']
            data = json.loads(data)
            id = int(data['id'])
            title = str(data['title'])
            description = str(data['description'])
            target = str(data['target'])
            cursor = db.cursor()
            # 这里注意，匹配的文本当中如果有引号的话可能与sql语句中的字符串引号叠加，然后执行失败。检查错误的方法是打印出sql语句，看看为什么不能执行
            sql = "insert into xueqiu_fangchan values('{}','{}','{}','{}')".format(id,title,description,target)
            # print(sql)
            cursor.execute(sql)
            db.commit()
            # print(res)
            time.sleep(random.randint(1,5))
db.close()
