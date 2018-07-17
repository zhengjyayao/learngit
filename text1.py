# coding:utf-8
import requests
from bs4 import BeautifulSoup

def getHtml(url):
    # 用get函数发送GET请求，获取响应
    res = requests.get(url)
    # 设置响应的编码格式utf-8（默认格式为ISO-8859-1），防止中文出现乱码
    return res

rest = getHtml("https://movie.douban.com/subject/26752088/comments?sort=new_score&status=P")
html = rest.text
rest.encoding = 'utf-8'
soup = BeautifulSoup(html,'html.parser')
#alinks = soup.select('.short')
#autos = soup.select(".comment-info")
#for item in alinks:
#    print(item.text)
#print(rest.text)
#for au in autos:
   # print(au)
 #   a = au.select('a')
  #  print(a[0].text)

all = soup.select('.comment-item')
for item in all:
    aus =  item.select('.comment-info')
    au = aus[0].select('a')
    con = item.select('.short')
    print(au[0].text)
    print(con[0].text)