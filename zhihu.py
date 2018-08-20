import requests,re
url = ' https://www.zhihu.com/api/v3/feed/topstory?action_feed=True&limit=7&session_token=f4e5ca04a8509f37e37c98d8b6893b37&action=down&after_id={}&desktop=true'
headers = {
'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}
# for i in range(5):
html = requests.get(url.format(34), headers = headers)
print(url.format(34))
for i in html.json()['data']:
    if i['target']:
        print(i['target']['question']['title'])
        print(i['target']['excerpt'])

