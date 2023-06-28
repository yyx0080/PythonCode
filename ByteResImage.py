#用于绘制代码量可视化的文件
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np

VersionName = []#版本名称
FileCount = []#文件计数
ByteCount = []#代码量统计

def ReadFile():
    file_path = 'C:\PythonCode\ByteResult.txt'  # 替换为你的文件路径
    skipFirst = True
    with open(file_path, 'r') as file:
        for line in file:
            #要去除第一行
            if(skipFirst == False):
                line = line.strip()  # 去除行尾的换行符和空白字符
                # 在这里对每一行进行操作，例如打印或进行处理
                sline = line.split(" ")
                VersionName.append(sline[0])
                filecount = int(sline[1])
                FileCount.append(filecount)
                bytecount = int(sline[2])
                ByteCount.append(bytecount)
                print(sline)
            else:skipFirst = False

def ReversALL():
    #反转所有
    VersionName.reverse()
    FileCount.reverse()
    ByteCount.reverse()
#这个函数绘制文件的统计图
def DrawFileCount():
    # 设置全局字体大小
    plt.rcParams['font.size'] = 12  # 设置字体大小为12
    plt.bar(VersionName,FileCount,color = "blue")
    x = np.arange(len(VersionName))
    plt.bar(x,FileCount)
    plt.xticks(x,VersionName, rotation='vertical',fontsize = 4)
    plt.ylim(65,max(FileCount)+5)
    plt.xlim(0, len(VersionName))  # 设置X轴的起始位置和结束位置
    # 添加标签和标题
    plt.xlabel('VersionName')
    plt.ylabel('FileCount')
    plt.title('Version&&FileCount')
    plt.savefig('FileCount.png',dpi=1200)
    plt.show()

#这个函数绘制文件的统计图
def DrawByteCount():
    # 设置全局字体大小
    plt.rcParams['font.size'] = 12  # 设置字体大小为12
    plt.bar(VersionName,ByteCount,color = "blue")
    x = np.arange(len(VersionName))
    plt.bar(x,ByteCount)
    plt.xticks(x,VersionName, rotation='vertical',fontsize = 4)
    plt.ylim(1500000,max(ByteCount)+5)
    plt.xlim(0, len(VersionName))  # 设置X轴的起始位置和结束位置
    # 添加标签和标题
    plt.xlabel('VersionName')
    plt.ylabel('ByteCount')
    plt.title('Version&&ByteCount')
    plt.savefig('ByteCount.png',dpi=1200)
    plt.show()

if __name__ == "__main__": #当程序执行时候,这也是整个程序的入口
    ReadFile()
    ReversALL()
    #开始绘图
    DrawFileCount()
    DrawByteCount()
