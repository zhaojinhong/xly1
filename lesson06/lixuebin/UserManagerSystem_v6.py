'''
3.1 将列表转换为字典
3.2 分页 --> 根据page和pagesize 进行分页并优雅输出
3.3 持久化数据
3.4 异常处理
3.5 优雅格式化输出
3.6 支持导出数据到csv --> 判断文件是否存在 --> 提示成功或失败
3.7 记录登陆日志 --> 登陆成功 --> log/login.log  登陆失败 --> log/loginFail.log
3.8 记录操作日志 --> add, update, delete, clear 进行记录
3.9 统计用户数量
3.10 清空用户 --> 临时清空 --> 可以reload加载 --> 永久清空 --> 直接修改文件永久清空
3.11 支持从cvs中导入数据 --> 文件存在 --> 文件格式校验 --> 重复数据校验

4.1 改写函数

5.1 数据持久化到MySQL数据库
5.2 使用configparser模块读取配置文件
'''

# 标准模块
import sys
import json
import os
from datetime import datetime
from prettytable import PrettyTable
import logging
import pymysql
import configparser

FIELDS = ['id', 'username', 'age', 'tel', 'email']


class Show(object):

    def printTalk(self, content):
        print(''' \n
        \t   ___________
        \t < {} >
        \t   -----------
        \t        \   ^__^
        \t         \  (oo)\_______
        \t            (__)\       )\/\\
        \t                ||----w |
        \t                ||     ||
        \t          ===================
        '''.format(content))

    def clearScreen(self):
        '''
        清屏
        :return:
        '''
        os.system('clear')

    def actionGuide(self):
        '''
        操作指引
        :return:
        '''
        try:
            TAB = PrettyTable()
            print('\n\t\033[5;31;47m北京第三区IT委提醒您：道路千万条，安全第一条。运维不规范，开发两行泪\033[0m\n')
            Title = ['Serial', 'Description', 'Command']
            TAB.field_names = Title
            row = [
                ['1', 'Add user info', '\033[31madd username age tel email.\033[0m']
                , ['2', 'Delete user', '\033[31mdelete username.\033[0m']
                , ['3', 'Update user info', '\033[31mupdate username set (age|tel|email) = new info.\033[0m']
                , ['4', 'Find user info', '\033[31mfind username.\033[0m']
                , ['5', 'Show tables', '\033[31mlist.\033[0m']
                , ['6', 'Pagination display', '\033[31mdisplay page 1 [pagesize 5].\033[0m']
                , ['7', 'Count of users', '\033[31mcount.\033[0m']
                # , ['8', 'Export csv file', '\033[31mexport [path/filename].Default "csv/UserData+unixtime.csv"\033[0m']
                # , ['9', 'From csv file import data', '\033[31mimport "path/filename"\033[0m']
                , ['8', 'Exit UserManager system', '\033[31mexit/Ctrl + C/Ctrl + D"\033[0m']
            ]
            for i in row:
                TAB.add_row(i)
            TAB.align['Description'] = 'l'
            TAB.align['Command'] = 'l'
            print(TAB)
            print()
        except Exception as  e:
            print("显示指导信息失败")

    def showTable(self, List):
        '''
        格式化: 接收列表
        :return: 返回格式化的表格
        '''
        try:
            TB = PrettyTable()
            TB.field_names = FIELDS
            for l in List:
                TB.add_row(l)
            return TB
            # TB.clear_rows()
        except ModuleNotFoundError:
            print("Prettytable 模块没有安装,请安装后再使用: pip3.x install prettytable.")
        except Exception as e:
            return False

    def mkDir(self):
        '''
        检测文件夹,无则创建文件夹
        :return:
        '''
        try:
            if os.path.exists('log') == False:
                os.mkdir('log')
        except Exception as e:
            print(e)


class User(object):

    def __init__(self, table='users', **kw):
        # self.name = kw['name']
        # self.age = kw['age']
        # self.tel = kw['tel']
        # self.email = kw['email']
        self.table = table
        self.tab = Show()


    def add(self, name, age, tel, email):
        try:
            sql = '''insert into {} (username,age,tel,email) values ('{}',{},'{}','{}');'''.format(self.table, name, age,
                                                                                                   tel, email)
            print(sql)
            db = DB()
            msg, ok = db.insert(sql)
            if ok:
                print(msg)
            else:
                print(msg)
            # 打印结果信息
        except Exception as  e:
            return False

    def delete(self, name):
        try:
            sql = '''delete from {} where username = '{}';'''.format(self.table, name)
            db = DB()
            msg, ok = db.delete(sql)
            if ok:
                LOG("log/action.log", '{} has been deleted!'.format(name))
                print(msg)
            else:
                LOG("log/action.log", 'Delete {} failed!'.format(name))
        except Exception as  e:
            return False

    def update(self, name, field, value, ):
        try:
            sql = '''update {} set {}='{}' where username='{}';'''.format(self.table, field, value, name)
            db = DB()
            msg, ok = db.update(sql)
            if ok:
                self.find(self.name)
                return msg, True
            else:
                return msg, False
        except Exception as e:
            print('\033[5;31m Please input "update {} set (age|tel|email) = new data!\033[0m"'.format(name))

    def find(self, name):
        '''
        查找用户
        :return:
        '''
        Find_List = []
        # if len(info) != 2:
        #     print('\033[5;31m Please enter "find  username" to find user!\033[0m')
        sql = '''select * from {} where username = '{}';'''.format(self.table, name)
        db = DB()
        msg, ok = db.select(sql)
        if ok:
            self.tab.showTable(msg)
            print("\n\033[32m There are a total of \033[5;32m{}\033[0m \033[32musers\033[0m".format(
                len(msg)))
        else:
            print(msg)

    def count(self):
        try:
            sql = '''select count(*) from {};'''.format(self.table)
            db = DB()
            msg, ok = db.select(sql)
            if ok:
                self.show.printTalk("共\033[5;32m{}\033[0m个用户".format(msg[0][0]))
                return True
            else:
                return False
        except Exception as e:
            print(e)

    def list(self):
        try:
            sql = '''select * from {}'''.format(self.table)
            db = DB()
            db.select(sql)
            # print(msg)
            # if type(msg) == list:
            #     self.tab.showTable(msg)
            #     print("\n\033[32m There are a total of \033[5;32m{}\033[0m \033[32musers\033[0m".format(
            #         len(msg)))
            #     msg.clear()
            #     return True
            # else:
            #     return False
        except Exception as e:
            return False

    def display(self, page, pagesize=5, table='users'):
        i = page
        j = pagesize
        sql = '''select * from {}'''.format(table)
        db = DB()
        PageList, ok = db.insert(sql)
        Lth = len(PageList)
        print(PageList)
        if ok:
            # 分页
            if j * i <= Lth + 1:
                Page = Lth[j * (i - 1):j * i]
                self.tab.showTable(Page)
                return True
            elif j > len(PageList):
                Page = PageList[j * (i - 1):]
                self.tab.ShowTable(Page)
                return True, j, i
            elif j * i - j < len(PageList):
                Page = PageList[j * i - j:]
                self.tab.showTable(Page)
                return True, j, i
            else:
                return False, j, i
        else:
            return False


class Auth(object):

    def __init__(self, username):
        self.username = username

    def login(self, password):
        try:
            adminInfo = ("51reboot", "123456")
            if self.username == adminInfo[0].strip() and password == adminInfo[1]:
                return True
            else:
                return False
        except Exception as  e:
            return False

    def session(self):
        while True:
            # 业务逻辑
            try:
                info = input("\n\033[1;31;47m 请开始你的表演 \033[0m\n\t:")
                info_list = info.split()
                action = info_list[0]
            except KeyboardInterrupt:
                sys.exit(0)
            # string -> list
            except Exception as e:
                print(
                    '\033[5;31m You input format is error. Please input (add|delete|update|find|count|list|clear|export|import|display) (username age tel email)!\033[0m')
                continue
            #     #
            # else:
            #     global Data
            #     Data = info_list[1:]

            Log = LOG()
            if action == "add":
                if len(info_list) != 5:
                    print("输入长度不正确,请输入:add username age tel email")
                    continue
                try:
                    Ac = User()
                    print(Ac)
                    Ac.add(info_list[1], info_list[2], info_list[3], info_list[4])
                    # Log.debug('log/Action.log', 'User {} has been added!'.format(info_list[1]))
                except Exception as  e:
                    print(e)
            elif action == "delete":
                if len(info_list) != 2:
                    print("输入长度不正确,请输入:delete username")
                    continue
                Ac = User()
                Ac.delete(info_list[1])
                Log.debug('log/Action.log', 'User {} has been deleted!'.format(info_list[1]))
            elif action == "update":
                if info_list[0] == 'update' and info_list[3] == 'set':
                    Ac = User(name=info_list[1])
                    Ac.update(info_list[4], info_list[-1])
                    Log.debug('log/Action.log', 'User {} has been update!'.format(info_list[1]))
                else:
                    print("输入错误,请输入:update username set oldValue = newValue")
            elif action == "list":
                # 如果没有记录， 那么提示为空
                try:
                    Ac = User()
                    Ac.list()
                except Exception as e:
                    print(e)
            elif action == "find":
                Ac = User()
                Ac.find(info_list[1])
            # 统计用户数量
            elif action == "count":
                Ac = User()
                Ac.count()
            # 分页实现
            elif action == 'display':
                if 'pagesize' in info_list:
                    Ac = User()
                    Ac.display(info_list[2], info_list[-1])
                else:
                    Ac = User()
                    Ac.display(info_list[2])
            elif action == "exit":
                self.logout()
            elif action == "help":
                show = Show()
                show.actionGuide()

            else:
                print("\033[5;31m invalid action.\033[0m")

    def logout(self):
        act = Show()
        act.clearScreen()
        act.printTalk("欢迎下次光临")
        Log = LOG()
        Log.debug('log/login.log', 'User {} has been logout!'.format(self.username))
        sys.exit(0)


class DB(object):


    def __init__(self):
        self.host: str = self.MyConn().get('mysqld', 'host')
        self.username: str = self.MyConn().get('mysqld', 'username')
        self.password: str = self.MyConn().get('mysqld', 'password')
        self.port: int = self.MyConn().get('mysqld', 'port')
        self.database: str = self.MyConn().get('mysqld', 'database')
        self.connect = pymysql.connect(
            host=self.host,
            username=self.username,
            password=self.password,
            port=self.port,
            database=self.database
        )
        self.cursor = self.connect.cursor()


    def MyConn(self, filename='mysql.ini'):
        try:
            config = configparser.ConfigParser()
            config.read(filename)

            return config
        except Exception as e:
            return False

    def select(self, sql):
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            datalist = []
            print(datalist)
            for i in data:
                datalist.append(list(i))
                print(datalist)
            return datalist, True
        except Exception as e:
            print('\033[5;31m User list is None! Please add user info!\033[0m')
            return e, False
        finally:
            self.cursor.close()
            self.connect.close()

    def insert(self, sql):
        if not self.connect:
            return 'conn is failed.', False
        try:
            self.cursorr.execute(sql)
            self.connect.commit()
            return "\n\033[1;32m Add user success.\033[0m", True
        except Exception as e:
            self.connect.rollback()
            return e, False
        finally:
            self.cursorr.close()
            self.connect.close()

    def update(self, sql):
        if not self.connect:
            return 'conn is failed.', False
        try:
            self.cursor.execute(sql)
            if self.cursor.rowcount == 0:
                return 'User is not exists,update failed!', False

            self.connect.commit()
            return 'update success', True
        except Exception as e:
            self.connect.rollback()
            return e, False
        finally:
            self.cursor.close()
            self.connect.close()

    def delete(self, sql):
        if not self.connect:
            return 'conn is failed.', False
        try:
            self.cursor.execute(sql)
            if self.cursor.rowcount != 1:
                return '"\033[5;31m This UserName is not exist! Please reinput !\033[0m"', False
            else:
                self.connect.commit()
                return 'delete success!', True

        except Exception as e:
            self.connect.rollback()
            return e, False
        finally:
            self.cursor.close()
            self.connect.close()


class LOG(object):


    def __init__(self):
        self.logger = logger = logging.getLogger('UserManagerSystem')

    def debug(self, logfile, message):
        '''
        定义log函数
        :return:
        '''
        # 创建一个logger

        self.logger.setLevel(logging.DEBUG)

        # 建立一个filenhandler把日志记录在文件,级别debug
        fl = logging.FileHandler(logfile)
        fl.setLevel(logging.DEBUG)

        # 设置日志格式
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(message)s")
        fl.setFormatter(formatter)

        # 将handler添加在logger对象中
        self.logger.addHandler(fl)
        self.logger.debug(message)


def logic():
    INIT_FAIL_CNT = 0
    MAX_FAIL_CNT = 3
    try:
        while INIT_FAIL_CNT < MAX_FAIL_CNT:
            try:

                username = input("\n\033[1;33;44m Please input your username (default:51reboot) \033[0m\n:")
                password = input("\n\033[1;33;41m Please input your password (default:123456) \033[0m\n:")
                act = Show()
                act.clearScreen()
            except Exception as e:
                print(e)
            ac = Auth(username)
            if ac.login(password):
                # Log = LOG()
                # Log.debug('log/login.log', '{} is loged in!'.format(username))
                show = Show()
                show.actionGuide()
                # 如果输入无效的操作，则反复操作, 否则输入exit退出
                ac.session()
            else:
                # 带颜色闪烁
                try:
                    print("\033[5;31m username or password error.\033[0m")
                    # Log = LOG()
                    # Log.debug('log/login.log', '{} is loged fialed!'.format(username))
                    INIT_FAIL_CNT += 1
                except Exception as e:
                    print(e)
        print("\n\033[1;31m Input {} failed, Terminal will exit.\033[0m".format(MAX_FAIL_CNT))
    except KeyboardInterrupt:
        show = Show()
        show.printTalk('非正常退出')
    except Exception as e:
        print(e)


def main():
    logic()


if __name__ == '__main__':
    main()
