#!/usr/bin/python
import sys
from utils import add_user,del_user,get_list,get_pageinfo,find_info,update_info,csv_export,init_info,save_info,load_info

FILENAME = "dic.txt"
help_info = '''---------------------------------------------
命令：
> 增: add monkey 12 132xxx monkey@51reboot.com
> 删: delete monkey
> 改: update monkey set age = 18
> 搜: find monkey
> 查: list
>分页: display page 1 pagesize 5
>导出：export
---------------------------------------------
'''

def logic():
    # 读取文件
    load_info(FILENAME)
    # 如果输入无效的操作，则反复操作, 否则输入exit退出
    while True:
        try:
            #初始化判断
            init_info()
            # 业务逻辑
            info = input("\033[1;35mPlease input your operation: \033[0m")
            # string -> list
            info_list = info.split()
            action = info_list[0]
            if action == "add":
                res = add_user(info_list)
                print(res)
                #最后保存变量到文件
                save_info(FILENAME)
            elif action == "delete" or action == "del":
                # .remove
                res = del_user(info_list)
                print(res)
                save_info(FILENAME)
            elif action == "find":
                res = find_info(info_list)
                print(res)
            elif action == "update":
                res = update_info(info_list)
                print(res)
                save_info(FILENAME)
            elif action == "list":
                res = get_list(info_list)
                print(res)
            elif action == "display":
                res = get_pageinfo(info_list)
                print(res)
            elif action == "export":
                res = csv_export()
                print(res)
            elif action == "help" or action == "h":
                print(help_info)
            elif action == "exit":
                sys.exit(0)
            else:
                print("\033[1;36m输入错误，请输入 help 查看帮助！\033[0m\n")
        # except IndexError:
        #     print('\033[1;36m[Errno] list index out of range.\033[0m\n')
        # except FileNotFoundError:
        #     print('\033[1;36m[Errno] No such file or directory.\033[0m\n')
        # except TypeError:
        #     print('\033[1;36m[Errno] Type Error.\033[0m\n')
        # except KeyError:
        #     print('\033[1;36m[Errno] Key Error.\033[0m\n')
        except Exception as e:
            print(e)