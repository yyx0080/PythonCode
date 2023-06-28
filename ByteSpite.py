#引入模块
import string
import urllib.request

from bs4 import BeautifulSoup #网页解析，获取数据的包
import re #正则表达式
import urllib3
import sqlite3 #进行sqlite数据库操作
from lxml import html

#首先从文件中读入版本号，并且拼接为URL然后返回
def GetURL(versionURL):
    URL_S = "https://elixir.bootlin.com/linux/"
    URL_E = "/source/net/ipv4"

    URL = URL_S + versionURL + URL_E
    #print(URL)
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

#网页解析函数,会返回文件总数，以及字节
def ResolverHtml(html):
    #定义正则表达式
    findByte = re.compile(r'<td><a tabindex="-1" class="size" href="(.*?)">(.*?)</a></td>')
    ByteALL = re.findall(findByte, html)
    #接下来累计数值大小,文件个数
    count = 0 #记录文件个数
    byte_count = 0#记录字节数量
    for item in ByteALL:
        if(item[1] != ''):
            count = count + 1
            #去除bytes
            s = str(item[1])
            s = s[:-6]
            #再次转为整型
            byte_count += int(s)
    #返回文件数量，以及字节
    DataALL = []
    DataALL.append(count)
    DataALL.append(byte_count)
    return  DataALL

def Test(DataAll):
    print(DataAll)




if __name__ == "__main__": #当程序执行时候,这也是整个程序的入口
    file = open('ByteResult.txt', mode='w')
    file.write("版本号 | 文件数量 | 总代码量"+"\n")
    with open("MainVersionInfo.txt", "r") as f:
        versionData = []
        for line in f.readlines():
            line = line.strip('\n')
            versionData.append(line)

    #这一段测试用
    #URL = GetURL(versionData[15])
    #html = GetHtml(URL)
    #data = ResolverHtml(html)
    #Test(data)
    #先爬个30个看看时间要多少
    ##
    ByteData = []
    for url in versionData:
        #先取得URL
        URL = GetURL(url)
        #放入网页解析函数中，并且解析
        html = GetHtml(URL)
        #获取数据
        data = ResolverHtml(html)
        ByteData.append(data)
        #要在这里写入，这样才有版本数据
        a = data[0]
        b = data[1]
        c = str(a)+" "+str(b)
        res = url+" "+c
        print(res)
        file.write(res+"\n")

    for byteData in ByteData:
        print(byteData)




