import requests
from  bs4 import BeautifulSoup
import re
###
#此代码只适应烟台大学教务系统
#
##
def getHTMLText(url, paydata):
    try:
        req = requests.session()
        r = req.post(url, data=paydata)
        r.raise_for_status()
        print(req.cookies)
        deom = r.text
        soup = BeautifulSoup(deom,'html.parser')
        pid = soup.find_all('a', {'target': '_blank'})
        for i in pid:
            url2=i.get('href')
        r2 = req.get(url2)
        deom1 = r2.text
        mod = BeautifulSoup(deom1,'html.parser')
        print(mod.find_all('a', )[2].string)
        url3 = "http://portal.ytu.edu.cn/mhpd/grsy"+mod.find_all('a',)[2]['href'][1:]
        r3 = req.get(url3)
        mod_url3 = r3.text
        soup_url3 = BeautifulSoup(mod_url3,'html.parser')
        # print(soup_url3.find_all('script', )[0].string)
        url4 = soup_url3.find_all(string = re.compile("202.194.116.35"))[0][27:100]

        req1 = requests.session()
        r4=req1.post(url4)
        r4_cooc=dict(req1.cookies)
        # print(r4_cooc)
        r4_ben = requests.post("http://202.194.116.35/xkAction.do?actionType=6", cookies=r4_cooc)
        r4_ben.encoding =r4_ben.apparent_encoding

        return r4_ben.text
    except:
        return "产生异常"


if __name__ == '__main__':
    paydata = {'user': '你的学号', 'password': '你的密码'}
    url = "http://portal.ytu.edu.cn/Login"
    print(getHTMLText(url, paydata))
