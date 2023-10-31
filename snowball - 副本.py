# -*-coding=utf-8-*-
#抓取雪球的收藏文章
__author__ = 'Rocky'
import requests,re,json,time
import http.cookiejar as cookielib
from toolkit import Toolkit
from lxml import etree
from bs4 import BeautifulSoup

url='https://xueqiu.com/snowman/login'
session = requests.session()

session.cookies = cookielib.LWPCookieJar(filename="cookies")
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie can't load")

agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
headers = {'Host': 'xueqiu.com',
           'Referer': 'https://xueqiu.com/',
           'Origin':'https://xueqiu.com',
           'User-Agent': agent}
account=Toolkit.getUserData('data.cfg')
print(account['snowball_user'])
print(account['snowball_password'])

data={'username':account['snowball_user'],'password':account['snowball_password']}
s=session.post(url,data=data,headers=headers)
print(s.status_code)
#print s.text
session.cookies.save()
#bing_url = 'https://xueqiu.com/u/4104161666/page/'
bing_url = 'https://xueqiu.com/u/4104161666'
#for i in range(1,120):
for i in range(1,2):
    #cur_page = bing_url + str(i)
    cur_page = bing_url
    response= session.get(cur_page)
    if not response:
        exit()
        
    soup = BeautifulSoup(response.content,"html.parser")    

    #文章item
    soup_items= soup.findAll("article",{"class":"timeline__item"})
    for item in soup_items:
        sticks = soup.findAll("span",{"class":"timeline__item__tag--stick"})
        if not sticks:
            #文章标题
            doc_title = soup.findAll("h3",{"class":"timeline__item__title"})
            doc_cont = soup.findAll("div",{"class":"timeline__item__content timeline__item__content--longtext"})
            url_cont = doc_cont.a
            url = url_cont.get('href')
