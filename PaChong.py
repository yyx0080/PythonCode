#引入模块
import urllib.request

from bs4 import BeautifulSoup #网页解析，获取数据的包
import re #正则表达式
import urllib3
import sqlite3 #进行sqlite数据库操作
from lxml import html


#先爬出所有小版本标号并且保存
def getVersionNum():
    versionUrl = "https://elixir.bootlin.com/linux/v2.6.39.4/source/net/ipv4"#用于爬出版本号的URL
    request = urllib.request.Request(versionUrl)
    html=""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

#处理输出版本号的函数,需要接受一下html
def ResovleVersion(html_t):
    #制定正则表达式
    findVersionNum = re.compile(r'<li class="li-link"><a href="(.*?)">(.*?)</a></li>')
    versionNums = re.findall(findVersionNum,html_t)
    f = open('versionInfo.txt',mode='w')
    #只需要版本号即可
    #遍历打印出版本号
    for i in versionNums:
        #这里已经输出了所有的版本号，我们不需要没用v开头的
        #因为没有v开头的版本太老了，没参考价值
        if(i[1][0] == 'v'):
            #接下来剔除大版本号
            if(len(i[1]) > 4):
                #接下来剔除v2.5版本以后的
                if(i[1][1] == '2' and i[1][2] == '.' and i[1][3] == '5'):
                    #print(i[1])
                    j = 1
                else:
                    #写入我们要的版本号中
                    f.write(i[1]+"\n")
                    print(i[1])


if __name__ == "__main__": #当程序执行时候,这也是整个程序的入口
    html = getVersionNum()
    #print(html)
    ResovleVersion(html)
    print("结束")



