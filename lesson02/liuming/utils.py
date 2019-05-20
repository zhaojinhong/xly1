#!/usr/bin/env python
# -*-encoding:utf-8-*-
# -------------------------------------------------------------------------------
# Name:         utils.py
# Description:  抽出公用模块
# Author:       Aaron
# Date:         2019/5/19
# -------------------------------------------------------------------------------


# 封装增删改查操作
class DataOperate(object):
    # 模拟一个结果数据列表， 所有操作只针对该列表
    global_data_list = ["name", "gender", "age", "job"]

    def __init__(self):
        print(self.global_data_list)

    # 添加，可批量添加数据到列表
    def add(self, data_list):
        # 筛选出全局数据列表已存在的数据
        already_exists_list = [i for i in data_list if i in self.global_data_list]
        # 筛选不存在于全局数据列表的新数据
        new_data_list = [i for i in data_list if i not in self.global_data_list]
        # 进行批量添加操作
        [self.global_data_list.append(i) for i in new_data_list]

        # 格式化输出
        msg = """
            \033[36mResult：{}\033[0m\n
            \033[36mSuccess: '{}' add success.\033[0m\n
            \033[31mFail: '{}' already exist, add operation is failing.\033[0m
        """.format(self.global_data_list, ','.join(map(str, new_data_list)), ','.join(map(str, already_exists_list)))
        print(msg)

    # remove直接删除值，可批量删除列表中数据
    def delete(self, data_list):
        # 循环出存在和不存在于全局数据列表的元素分别存入俩个列表
        nonexistent_data = []
        for i in data_list:
            if i not in self.global_data_list:
                nonexistent_data.append(str(i))
                data_list.remove(i)
        exist_data = data_list

        error_msg = "\033[31mError: {} don't exist, u needn't to delete.\033[0m".format(nonexistent_data) if nonexistent_data else ""
        # 判断可进行删除的元素是否不为空
        if exist_data:
            # 进行批量删除
            [self.global_data_list.remove(i) for i in exist_data]
            successful_msg = "\033[36mSuccess: delete {} is successful.\033[0m".format(len(exist_data), '、'.join(map(str, exist_data)))
        else:
            successful_msg = "\033[36mSuccess: nothing need to delete.\033[0m".format(len(exist_data), '、'.join(map(str, exist_data)))

        msg = """
            \033[36mResult：{}\033[0m\n
            {}\n
            {}
        """.format(self.global_data_list, successful_msg, error_msg)
        print(msg)

    # 通过id更新数据列表
    def update(self, data_list):
        """
        :param data_list: [(list_index, new_value), (list_index, new_value), ...]
        :return:
        """
        try:
            for t in data_list:
                self.global_data_list[int(t[0])] = t[1]
        except Exception as e:
            print("\033[31mError:\n{}\033[0m".format(e))

        print("\033[36mafter update, new data_list:{}\n\033[0m".format(self.global_data_list))

    # 可通过索引（精确）查找， 切片（模糊）查找
    def find(self, *args):
        result = []
        if len(args) < 1:
            print("\033[31mError:  takes exactly one argument (0 given)\033[0m")
        elif len(args) == 1:
            index = args[0]
            if index > len(self.global_data_list):
                print("\033[31mIndex exceeds list length\033[0m")
                return

            result = self.global_data_list[index]
            print("\033[36mHere is the data you got.\033[0m")
            print("\033[36m{}\033[0m".format(result))
            print("\033[36m-\033[0m" * 60)
            return
        elif len(args) == 2:
            start, stop = args
            result = self.global_data_list[start:stop]
        elif len(args) == 3:
            # print(args)
            start, stop, step = args
            result = self.global_data_list[start:stop:step]
        else:
            print("\033[31mError: parameters is too many.\033[0m")
            return

        if result:
            print("\033[36mHere is the data you got.\033[0m")
            for i in result:
                print("\033[36m{}\033[0m".format(i))
            print("\033[36m-\033[0m" * 60)
        else:
            print("\033[31mYou don't get anything.\033[0m")

    # 列出所有数据
    def list(self):
        if not self.global_data_list:
            print("\033[36mData is empty，add a new,please.\033[0m")
        else:
            for i in enumerate(self.global_data_list):
                    print("\033[36mIndex: {:<10}\tItem: {}\033[0m".format(i[0], i[1]))
            print("\033[36m-\033[0m" * 60)
