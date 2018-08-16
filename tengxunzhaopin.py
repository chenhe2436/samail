import requests
from bs4 import BeautifulSoup
from math import ceil

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}


# 获取岗位页数
def getJobPage(url):
    ret = requests.get(url, headers=header)
    ret.encoding = "utf-8"  # 解决乱码问题
    html = ret.text
    soup = BeautifulSoup(html, 'html.parser')
    # 获取岗位总数，< span class ="lightblue total" > 512 < / span >
    totalJob = soup.select('span[class="lightblue total"]')[0].text
    jobPage = ceil(int(totalJob) / 10)
    return jobPage


def getJobOrder(url):
    ret = requests.get(url, headers=header)
    ret.encoding = "utf-8"  # 解决乱码问题
    html = ret.text
    soup = BeautifulSoup(html, 'html.parser')
    # 工作职责
    jobRequests = soup.select('ul[class="squareli"]')[0].text
    # 工作要求
    jobOrder = soup.select('ul[class="squareli"]')[1].text
    return jobRequests, jobOrder


# 获取岗位信息
def getJobInfo(url):
    myfile = open("tencent_job.txt", "a", encoding='gb18030', errors='ignore')  # 解决乱码问题
    ret = requests.get(url, headers=header)
    ret.encoding = "utf-8"  # 解决乱码问题
    html = ret.text
    soup = BeautifulSoup(html, 'html.parser')
    jobList = soup.find_all('tr', class_=['even', 'odd'])
    for job in jobList:
        # url
        jobUrl = "https://hr.tencent.com/" + job.select('td:nth-of-type(1) > a')[0]['href']
        # 职位名称
        jobName = job.select('td:nth-of-type(1) > a')[0].text
        # 人数
        jobPeople = job.select('td:nth-of-type(3)')[0].text
        # 地点
        jobAddre = job.select('td:nth-of-type(4)')[0].text
        # 发布时间
        jobTime = job.select('td:nth-of-type(5)')[0].text
        # 工作职责
        jobRequests = getJobOrder(jobUrl)[0]
        # 工作要求
        jobOrder = getJobOrder(jobUrl)[1]

        #print(jobName, jobUrl, jobAddre, jobPeople, jobTime, jobRequests, jobOrder)

        tt = jobName + " " + jobUrl + " " + jobAddre + " " + jobPeople + " " + jobTime + " " + jobRequests + " " + jobOrder
        myfile.write(tt + "\n")


if __name__ == '__main__':
    mainurl = 'https://hr.tencent.com/position.php?keywords=python'
    jobPage = getJobPage(mainurl)
    print(jobPage)
    for page in range(jobPage):
        pageUrl = 'https://hr.tencent.com/position.php?keywords=python&start=' + str(page * 10) + '#a'
        print("第" + str(page + 1) + "页")
        getJobInfo(pageUrl)

