# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/5/26'
#    __Desc__ =  测试测试  刷新自己的博客的浏览量

import urllib.request,re
from bs4 import BeautifulSoup
import href

def getHtml(url,headers):
    req = urllib.request.Request(url,headers=headers)
    page = urllib.request.urlopen(req)
    html = page.read()
    return html

def parse(data):
    content = BeautifulSoup(data,'lxml')
    return content

def getReadNums(data,st):
    reg = re.compile(st)
    return re.findall(reg,data)

# url = 'http://blog.csdn.net/my201558503128/article/details/70851346'
headers = {
    'referer':'http://blog.csdn.net/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'
}

j = 0
a = href.main('__main__')
for j in range(len(a)):
    url = 'http://blog.csdn.net' + a[j]
    print(url)
    i = 0
    while i<10:
        html = getHtml(url,headers)
        content = parse(html)
        result = content.find_all('span',class_='link_view')
        print(result[0].get_text())
        i = i +1
