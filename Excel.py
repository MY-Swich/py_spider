import xlrd
import re
import os
###
#为了更简单的计算加权平均分，特地写了这段代码^-^
#
#
###
def jisuan(lb):
    sum = 0
    xf = 0
    for i in range(nrows):
        for j in range(ncols):
            if i >= 5 and j >= 5 and i <= 50 and j <= int(lb):
                s = m[i][j]
                if (s != "-"):
                    xf = xf + float(m[3][j])
                    sum = sum + float(s) * float(m[3][j])
        if i >= 5:
            print(m[i][4] + str(sum / xf))
        sum = 0
        xf = 0

while 1:
    path = input("请输入文件路径：")
    p1 = os.path.exists(path)
    if p1:
        data = xlrd.open_workbook(path)
        table = data.sheets()[0]
        nrows = table.nrows
        ncols = table.ncols
        arr = []
        m = []
        for i in range(nrows):
            for j in range(ncols):
                a = table.cell_value(i, j)
                # if type(a) == str: #比较类型
                #     a=a.strip() #去除空格
                a = str(a)
                a = a.strip()  # 去除空格
                # 正则表达式去除字符串中的汉字
                # if re.search(r'\d', a):
                a = re.sub(r'\s.*$', "", a)
                if a == '优':
                    a = 95
                elif a == '良':
                    a = 85
                elif a == '中':
                    a = 75
                elif a == '不及格':
                    a = 55
                elif a == '及格':
                    a = 65
                elif a == '零分':
                    a = 0

                arr.append(a)
            m.append(arr)
            arr = []
        while 1:
            lb = input("请输入计算终止列：")
            if int(lb)<5 or int(lb) >ncols:
                print("输入范围有误，请重新输入")
            else:
                jisuan(lb)
                print("计算过程可能存在误差，请认真核实最后成绩")
                break
    else:
        # print("没有找到文件")
        print("找不到文件")