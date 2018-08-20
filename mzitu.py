import requests,re,os,pymysql
from urllib import  request
# origin url http://www.mzitu.com/page/2/
# son url http://www.mzitu.com/145485/2
# img url 'http://i.meizitu.net/2018/08/05a02.jpg'
db = pymysql.connect('127.0.0.1','root','chenhe','pachong')
cursor = db.cursor()
sql = 'select ip,port from url_true'
cursor.execute(sql)
data_tuple = cursor.fetchall()
cursor.close()
db.close()
url_origin = 'http://www.mzitu.com/page/{}/'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}
for i in range(1,6):
    try:
        html_origin_str = requests.get(url_origin.format(i),headers=headers, timeout=3).text
        pat = re.compile(r'<a href="(.*?)".*?alt=\'(.*?)\'.*?\1')
        url_son_list = pat.findall(html_origin_str)
        for url_son in url_son_list:
            if not os.path.exists(url_son[1]):
                os.makedirs(url_son[1])
            for j in range(1,21):
                html_son_str = requests.get(url_son[0]+'/'+str(j),headers=headers,).text
                # print(html_son_str)
                pat = re.compile(r'<img src="(.*?)"', re.S)
                url_img_list = pat.findall(html_son_str)
                print(url_img_list)
                if url_img_list:
                    data = requests.get(url_img_list[0],headers=headers).content
                    print(data)
                    print('正在下载图片'+url_son[0])
                    with open(url_son[1] + '/' + url_img_list[0].split('/')[-1],'wb') as f:
                        f.write(data)
                else:
                    continue
    except:
        # print('代理失效，更换代理继续')
        continue

