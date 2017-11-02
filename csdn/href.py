import requests
from bs4 import BeautifulSoup

def getHtml():
    r = requests.get('http://blog.csdn.net/my201558503128?viewmode=contents')
    return r.text

def parse(data):
    content=BeautifulSoup(data,'lxml')
    return content

def count():
    html = getHtml()
    cut_span = parse(html)
    a=0
    for result in cut_span.find_all('a', title="阅读次数"):
        a=a+1
    return a

def main(__name__):
    if __name__ == '__main__':
        m = []
        html=getHtml()
        cut_span=parse(html)
        for result in cut_span.find_all('a',title="阅读次数"):
            # print(result.get('href'))
            m.append(result.get('href'))
        return m