import requests,re,time,random
import mysql_cunchu
for i in range(1,6):
    url = 'https://bj.5i5j.com/zufang/n{}/'.format(i)
    headers = {
    # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encoding':'gzip, deflate, br',
    # 'Accept-Language':'zh-CN,zh;q=0.9',
    # 'Cache-Control':'max-age=0',
    # 'Connection':'keep-alive',
    # 'Host':'bj.5i5j.com',
    # 'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    }
    html = requests.get(url,headers=headers)
    data_str = html.text
    print(data_str)
    pat = re.compile(r'"i_01"></i>.*?"i_01"></i>(.*?)·(.*?)·(.*?)·(.*?)·(.*?)<.*?"_blank">(.*?)<.*?> · (.*?)<.*?strong>(.*?)<', re.S)
    data_list = pat.findall(data_str) # [('4室2厅', ' 192.67平米', ' 南北 ', '中层/11层 ', '精装', '中关村 东南小区', '距离地铁海淀黄庄591米', '8600'), ('4室2厅', ' 192.67平米', ' 南北 ', '中层/11层 ', '精装', '五道口 地质大学', '距离地铁五道口848米', '14000'), ('4室2厅', ' 192.67平米', ' 南北 ', '中层/11层 ', '精装', '五道口 科汇小区', '距离地铁中关村1026米', '8500'),
    print(data_list)
    mysql_temp = mysql_cunchu.MysqlCunchu()
    sql = 'insert into woaiwojia(huxing,mianji,chaoxiang,louceng,zhuangxiu,weizhi,weizhixiangqing,jiage) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    print('正在储存第{}页信息'.format(i))
    for data_tuple in data_list:

        mysql_temp.mysql_excute(sql,data_tuple)
    print('储存完毕')
    time.sleep(random.randint(2,5))