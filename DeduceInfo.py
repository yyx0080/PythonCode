#这个程序来减少之前的versionInfo
#经实测，30个版本数据要爬7分钟
#总共4300个版本数据就要爬4300/30 * 7 =1003分钟
#总耗时 16.7h
#这个时间是无法忍受的，所以，这个程序的主旨在于选出具有代表性的版本

if __name__ == "__main__": #当程序执行时候,这也是整个程序的入口
    file = open('MainVersionInfo.txt', mode='w')
    with open("versionInfo.txt", "r") as f:
        versionData = []
        for line in f.readlines():
            line = line.strip('\n')
            versionData.append(line)
    a = 'v'
    b = '6'  # 第一个版本编号
    c = '.'
    d = '4'  # 第二个版本编号
    e = '-'
    f = ''

    #接下来只留下具有代表性的版本
    for v in versionData:
        #取出前四个字，第一个肯定是v，不用取出
        if(v[1] == '6'):
            if(v[0] != a or v[1]!=b or v[2]!=c or v[3] != d):
                file.write(v + "\n")
                print(v)
                a = 'v'
                b = v[1]  # 第一个版本编号
                c = '.'
                d = v[3]  # 第二个版本编号
        else:
            if (v[0] != a or v[1] != b or v[2] != c or v[3] != d or v[4] != e):
                file.write(v + "\n")
                print(v)
                a = 'v'
                b = v[1]  # 第一个版本编号
                c = '.'
                d = v[3]  # 第二个版本编号
                e = v[4]


