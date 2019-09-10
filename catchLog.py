import xlwt
import re
import xlrd
from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator

#创建一个excel表
wb = xlwt.Workbook()
ws = wb.add_sheet('Sheet')

#创建好表头（需获取的标题信息）
ws.write(0, 0, 'time')
ws.write(0, 1, 'TopMem')
ws.write(0, 2, 'MemTotal')
ws.write(0, 3, 'MemAvailable')
ws.write(0, 4, 'MEM')
ws.write(0, 5, 'CPU')

#获取日志（全名）
filename = input("please enter the name of file :")

#遍历log，用正则表达式找出来所需数据
with open(filename,'r',encoding='ISO-8859-1') as f:
    row = 1
    for line in f:
        Time = re.findall('[0-9]{4}/[0-9]{2}/[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{4}',line)
        List = re.findall('\d{2,3}%|\d+KB', line)
        TM_MT_MA_MEM_CPU = re.findall('\d+',str(List))
        if Time and len(List):
            print(Time)
            print(TM_MT_MA_MEM_CPU)
            ws.write(row,0,Time)
            ws.write(row, 1, TM_MT_MA_MEM_CPU[0])
            ws.write(row, 2, TM_MT_MA_MEM_CPU[1])
            ws.write(row, 3, TM_MT_MA_MEM_CPU[2])
            ws.write(row, 4, TM_MT_MA_MEM_CPU[3])
            ws.write(row, 5, TM_MT_MA_MEM_CPU[4])
            row += 1
        else:
            continue
    TotalRows = row

#保存好生成的excel文件
wb.save('catchlog.xls')


#打开绘图数据的目标文件
data = xlrd.open_workbook(r'catchlog.xls')
read_sheet = data.sheets()[0]
listTime = []
listTopMem = []
listMemTotal = []
listMemAvaliable = []
listMEM = []
listCPU = []


#定义可能需要显示的图线（1条横轴表示时间，5条表示数据走势）
def Time():

    for rows in range(1,TotalRows):
        listTime.append(read_sheet.cell(rows, 0).value)

def TopMem():

    for rows in range(1, TotalRows):
        listTopMem.append(read_sheet.cell(rows, 1).value)

def MemTotal():

    for rows in range(1, TotalRows):
        listMemTotal.append(read_sheet.cell(rows, 2).value)

def MemAvaliable():

    for rows in range(1, TotalRows):
        listMemAvaliable.append(read_sheet.cell(rows, 3).value)

def MEM():

    for rows in range(1, TotalRows):
        listMEM.append(read_sheet.cell(rows, 4).value)

def CPU():

    for rows in range(1, TotalRows):
        listCPU.append(read_sheet.cell(rows, 5).value)

#暂时先调用显示横轴和一条折线
Time()
TopMem()

#横轴纵轴，横轴图例倾斜45°
plt.plot(listTime,listTopMem)
plt.xticks(rotation=45)

#图像标题，横轴纵轴，以及横轴间隔线密度
plt.title("LogCatch",fontsize=24)
plt.xlabel("Time",fontsize=3)
plt.ylabel("Value",fontsize=3)
x_major_locator = MultipleLocator(3)
plt.tick_params(axis='both',which='major',labelsize=5)

#生成并显示图像
#plt.axis([0,5000,0,100])
plt.savefig('Logcat.png',bbox_inches='tight',dpi=300)
plt.show()









