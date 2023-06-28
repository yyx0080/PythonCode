#这是一个ipv4具体更新信息的爬虫
#引入模块
import urllib.request

from bs4 import BeautifulSoup #网页解析，获取数据的包
import re #正则表达式
import urllib3
import sqlite3 #进行sqlite数据库操作
from lxml import html

def GetURL(n):
    #这里后面的ofs是200依次加上去的
    #总共到11800，因此要爬11800/200 = 59次
    #传入的参数n n*200拼接即可
    pos = n*200
    URL = "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/log/net/ipv4?ofs="+str(pos)
    print(URL)
    return URL
#返回HTML函数
def GetHtml(URL):
    request = urllib.request.Request(URL)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

#网页解析函数,会返回更新时间，更新内容，作者
def ResolverHtml(html):
    #定义正则表达式
    #print(html)
    findInfo = re.compile(r'<tr><td><span title=(.*?)>(.*?)</span></td><td><a href=(.*?)>(.*?)</a></td><td>(.*?)</td><td>(.*?)</td><td><span class=(.*?)>(.*?)</span>/<span class=(.*?)>(.*?)</span></td></tr>')
    InfoALL = re.findall(findInfo, html)
    #这样爬下来的数据要忽略只要
    #1 3 4 对应更新时间，更新内容，以及作者
    allInfo = []#总共的信息
    #接下来处理
    for info in InfoALL:
        #接下来只挑选ipv4的内容输出
        #print(info[1]+" "+info[3]+" "+info[4])
        s = str(info[3])
        t = 'ipv4'
        t2 = 'IPV4'
        resflag = t in s
        resflag2 = t2 in s
        if(resflag or resflag2):
            #print(info[1] + " " + info[3] + " " + info[4])
            allInfo.append(info[1] + " %" + info[3] + "% " + info[4])
            #接下来放到答案数组中即可
    for info in allInfo:
        file.write(info+"\n")





if __name__ == "__main__": #当程序执行时候,这也是整个程序的入口
    #先测试一下,第一个网页
    file = open('UpdataResult.txt', mode='w',encoding='utf-8')
    file.write("更新日期 | 更新内容 | 更新者姓名（%用作隔开符号）" + "\n")
    #接下来爬取全部的ipv4内容
    for i in range(0,60):
        #跳过10000这个
        if(i != 50):
            URL = GetURL(i)
            html = GetHtml(URL)
            ResolverHtml(html)


