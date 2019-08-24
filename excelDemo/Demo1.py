# coding: utf-8
import os
import csv
import xlrd

Org = 15
startNumber = 100
# file_dir = '/Users/superlk/Desktop/供电设备履历/巴海区间/一杆一档'
file_dir = '/Users/superlk/Desktop/供电设备履历/巴海区间/一跨一档'
# file_dir = '/Users/superlk/Desktop/供电设备履历/海南站/机走线/一杆一档/机走线一杆一档'


def file_name(file_dir):
    l = list()
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if not file.startswith('.~') and not file.startswith('~$'):
                file_name = file_dir + '/' + file
                source = read_excel(file_name)
                l.append(source)
    return l


def read_excel(file):
    ex = xlrd.open_workbook(file)
    sheet1 = ex.sheet_by_name('主设备信息')
    row = sheet1.nrows
    col = sheet1.ncols
    data = {}
    data['value'] = []
    for i in range(row):
        if i > 0:
            if i == 1:
                data['key'] = list(sheet1.row_values(i, 0, col))
            else:

                data['value'].append(list(sheet1.row_values(i, 0, col)))

    Data = []
    for v in data['value']:
        Data.append(dict(zip(data['key'], v)))

    # 处理 一级设备
    sheet2 = ex.sheet_by_name('一级')
    row2 = sheet2.nrows
    col2 = sheet2.ncols
    # print(row2, col2)
    data2 = {}
    Data2 = []
    data2['value'] = []
    for x in range(row2):
        if x == 0:
            data2['key'] = sheet2.row_values(x, 0, col2)
        else:
            l = sheet2.row_values(x, 0, col2)
            data2['value'].append(l)
    for s in data2['value']:
        Data2.append(dict(zip(data2['key'], s)))

    # print(Data,Data2)
    source = dict()
    source['main'] = Data
    source['first'] = Data2
    # print(source)
    return source


def write_csv(l):
    file = '/Users/superlk/Desktop/MainDeviceYKYD.csv'
    file1 = '/Users/superlk/Desktop/main_ykyd.csv'
    file2 = '/Users/superlk/Desktop/FirstDeviceYKYD.csv'
    file3 = '/Users/superlk/Desktop/first_ykyd.csv'
    with open(file, encoding='gbk') as f:
        # with open(file) as f:
        f_csv = csv.reader(f)
        f_csv_list = list(f_csv)

        num = len(f_csv_list)
    # datalist = formatData(data, f_csv_list[1], startNumber)

    with open(file2, encoding='gbk') as f2:
        # with open(file) as f2:
        f_csv2 = csv.reader(f2)
        f_csv_list2 = list(f_csv2)

        num = len(f_csv_list2)
    dataList, dataList2 = formatData(l, f_csv_list[1], f_csv_list2[1])

    with open(file1, 'a+', encoding='utf-8', newline='') as f1:
        writer = csv.DictWriter(f1, f_csv_list[1])
        writer.writeheader()
        writer.writerows(dataList)

    with open(file3, 'a+', encoding='utf-8', newline='') as f3:
        writer = csv.DictWriter(f3, f_csv_list2[1])
        writer.writeheader()
        writer.writerows(dataList2)

    print('write is success')


def formatData(l, csv_list, csv_list2):
    num = startNumber
    DataList = []
    DataList2 = []
    for i in l:
        data = i['main']
        data2 = i['first']
        for d in data:
            DataDict = {}
            for k, v in d.items():
                # for row in csv_list:
                if k in csv_list:
                    DataDict[k] = str(v)
                    if k == '设备编码':
                        DataDict[k] = num
                    if k == '拉线安装图号':
                        DataDict[k] = str(v) + "."

                elif k == '''跨号
（关联作业单查询）''':
                    DataDict['跨号 （关联作业单查询） '] = str(v)
                elif k == '''软横跨号/硬横梁
（关联作业单查询）''':
                    DataDict['软横跨号/硬横梁 （关联作业单查询）'] = str(v)
                elif k == '''相邻股道号
（关联作业单查询）''':
                    DataDict['相邻股道号 （关联作业单查询）'] = str(v)
                else:
                    print('主设备匹配错误keyK>>>', k)
                DataDict['组织 '] = Org

            DataList.append(DataDict)
            num2 = 1
            for d2 in data2:
                DataDict2 = {}
                for m, n in d2.items():
                    if m in csv_list2:
                        DataDict2[m] = str(n)
                    elif m == "投运时间":
                        DataDict2['投运日期'] = str(n)
                    elif m == '一级从设备编码':
                        DataDict2['设备编号'] = num * 1000 + num2
                        # print( ">>>>>",num2)
                    else:
                        print('一级匹配错误key>>>>>>', m, csv_list2)
                    DataDict2['主设备编号'] = num
                    DataDict2['组织'] = Org
                num2 += 1
                DataList2.append(DataDict2)

        num += 1

    return DataList, DataList2


def start(path):
    l = file_name(path)
    write_csv(l)


if __name__ == '__main__':
    start(file_dir)
    # write_csv(file_dir)
