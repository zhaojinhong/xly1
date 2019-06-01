# -*- coding:utf-8 -*-
# author: lyl
import csv
import check
import add
import logs

def save_user():
    # 配置标题
    user_list = [['id', 'name', 'age', 'tel', 'email']]
    # 检测文件是否异常，将txt数据写入列表
    tag, user_dict = check.user_dict()
    if tag:
        for i in user_dict.keys():
            user_list.append([user_dict[i]['id'], user_dict[i]['name'], user_dict[i]['age'], user_dict[i]['tel'],
                              user_dict[i]['email']])
    else:
        print(user_dict)
        return
    # 写入CSV文件
    with open('./user.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for list1 in user_list:
            csv_writer.writerow(list1)
    print("文件导出完毕, 文件名为：xxxx")


def load_user(info_list, role):
    load_tag = True
    # 检查用户权限
    if role != 'admin':
        print("\033[1;31mpermission denied\033[0m")
        return
    # 检查用户输入参数
    if len(info_list) != 2:
        print("\033[1;31m用户输入参数有误 eg: load filename\033[0m")
        return
    try:
        reader = csv.reader(open(info_list[1]))
    except FileNotFoundError as e:
        print("\033[1;31m文件不存在\033[0m")
        logs.error(e)
        return
    except IsADirectoryError as e:
        print("\033[1;31m输入有误，请输入文件\033[0m")
        logs.error(e)
        return
    try:
        for user_id, name, age, tel, email in reader:
            if load_tag:
                load_tag = False
                continue
            tag1, _, _ = check.user(name)
            if tag1:
                print("\033[1;31m {} 导入失败, id or username已存在\033[0m".format(name))
            else:
                user_list = [user_id, name, age, tel, email]
                add.user(user_list, role)

    except ValueError as e:
        print("\033[1;31m文件load失败，请检查文件内容\033[0m")
        logs.error(e)
        return
