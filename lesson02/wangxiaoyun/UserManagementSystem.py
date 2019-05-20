#!/usr/local/python36/bin/python3.6
#-*- coding: utf-8 -*-
'''
用户管理系统
Author: WangXiaoYun
'''

import sys,os,getpass

_StuDist = {}
_StuInfo = 'StuInfo.txt'
_Username = 'test'
_Password = 'test@123'
_UCount = 0

#判断用户信息文件是否存在
if os.path.exists(_StuInfo) == False:
    os.mknod(_StuInfo)

while True:
    _UCount += 1
    #用户密码次数校验
    if _UCount > 3:
        sys.exit('用户名或密码输入次数大于3次，程序退出.')
    else:
        _InUser = input('Username: ')
        _InPass = getpass.getpass('Password: ')
        if _InUser != _Username or _InPass != _Password:
            print('用户名或密码错误.')
        else:
            print('登录成功.')
            while True:    #选择菜单防重复登录
                print ('\n菜单: \n'
                       '1. 添加学生信息.\n'
                       '2. 删除学生信息.\n'
                       '3. 更新学生信息.\n'
                       '4. 搜索学生信息.\n'
                       '5. 显示所有学生信息.\n'
                       '6. 退出.\n')
                _Choose = int(input('Please Choose: '))
                if _Choose == 1:     #添加学生信息
                    print('Please Add Student Info. Format is "id,name,phone,company,address,email"')
                    _StuId = 'stu' + str(int(input('ID: ')))
                    _StuName = str(input('Name: '))
                    _StuPhone = int(input('Phone: '))
                    _StuCompany = str(input('Company: '))
                    _StuAddress = str(input('Address: '))
                    _StuEmail = str(input('Email: '))

                    for i in range(1,4):   #邮箱格式校验
                        if _StuEmail.find('@') == -1:
                            if i<=2:
                                print('Email必须包含@，格式输入有误，请重新输入')
                                _StuEmail = str(input('Email: '))
                            else:
                                sys.exit('Email格式输入错误次数过多，程序退出.')
                    print('\n输入的学生信息如下: \nID: {}, Name: {}, Phone: {}, Company: {}, Address: {}, Email: {}.\n'.format(_StuId,_StuName,_StuPhone,_StuCompany,_StuAddress,_StuEmail))
                    with open(_StuInfo, 'r') as fs:    #判断学生ID是否存在
                            for _Item in fs.readlines():
                                _Id,_Name,_Phone,_Company,_Address,_Email = _Item.split()
                                _StuDist[_Id] = [_Id,_Name,_Phone,_Company,_Address,_Email]
                            if _StuDist.__contains__(_StuId) == False:
                                _StuDist[_StuId] = [_StuName,_StuPhone,_StuCompany,_StuAddress,_StuEmail]
                                _StuWrite = _StuId+' '+_StuName+' '+str(_StuPhone)+' '+_StuCompany+' '+_StuAddress+' '+_StuEmail+'\n'
                                with open(_StuInfo, 'a') as fs:
                                    fs.write(_StuWrite)
                                    print('该学生ID {} 信息已添加到学生信息表中.\n'.format(_StuId))
                            else:
                                print('该学生ID {} 已经在学习信息表中，添加失败.\n'.format(_StuId))
                if _Choose == 2:
                    _StuId = 'stu' + str(int(input('请输入需要删除的学生ID: ')))
                    with open(_StuInfo, 'r') as fs:    #判断学生ID是否存在
                        for _Item in fs.readlines():
                            _Id,_Name,_Phone,_Company,_Address,_Email = _Item.split()
                            _StuDist[_Id] = [_Id,_Name,_Phone,_Company,_Address,_Email]
                        for j in range(1,4):    #输入次数校验
                            if _StuDist.__contains__(_StuId) == False:
                                if j <= 2:
                                    print('该学生ID {} 不存在.请重新输入.'.format(_StuId))
                                    _StuId = 'stu' + str(int(input('请输入需要删除的学生ID: ')))
                                else:
                                    sys.exit('学生ID 输入错误次数过多，程序退出.')
                        for _Row in _StuDist.keys():
                            if _StuId == _Row:
                                _Id,_Name, _Phone, _Company, _Address, _Email =_StuDist[_Row]
                                print('学生信息如下: \nID: {}, Name: {}, Phone: {}, Company: {}, Address: {}, Email: {}.\n'.format(_Id,_Name,_Phone,_Company,_Address,_Email))
                    _Result = str(input('是否删除 {} 的学生信息[Yy|Nn]:'.format(_Id))).lower()
                    if _Result == 'y':
                        with open(_StuInfo,'r') as fs:
                            _Lines = fs.readlines()
                        with open(_StuInfo,'w') as fs:
                            for _Line in _Lines:
                                if _StuId in _Line:
                                    continue
                                fs.write(_Line)
                            print('该学生ID {} 信息已删除.\n'.format(_StuId))
                    else:
                        print('已取消删除学生信息.')
                if _Choose == 3:
                    _StuId = 'stu' + str(int(input('请输入需要更新的学生ID: ')))
                    with open(_StuInfo, 'r') as fs:    #判断学生ID是否存在
                        for _Item in fs.readlines():
                            _Id,_Name,_Phone,_Company,_Address,_Email = _Item.split()
                            _StuDist[_Id] = [_Id,_Name,_Phone,_Company,_Address,_Email]
                        for j in range(1, 4):  # 输入次数校验
                            if _StuDist.__contains__(_StuId) == False:
                                if j <= 2:
                                    print('该学生ID {} 不存在.请重新输入.'.format(_StuId))
                                    _StuId = 'stu' + str(int(input('请输入需要更新的学生ID: ')))
                                else:
                                    sys.exit('学生ID 输入错误次数过多，程序退出.')
                        for _Row in _StuDist.keys():
                            if _StuId == _Row:
                                _Id, _Name, _Phone, _Company, _Address, _Email = _StuDist[_Row]
                                print('学生信息如下: \nID: {}, Name: {}, Phone: {}, Company: {}, Address: {}, Email: {}.\n'.format(_Id, _Name, _Phone, _Company, _Address, _Email))
                    while True:    #修改学生信息可防退出菜单.
                        print('\n菜单: \n'
                              '1. 更新学生姓名.\n'
                              '2. 更新学生电话.\n'
                              '3. 更新学生公司名.\n'
                              '4. 更新学生住址.\n'
                              '5. 更新学生Email.\n'
                              '6. 退出.\n')
                        _Num = int(input('请输入需要更新的学生信息编码: '))
                        if _Num == 1:
                            _Name = str(input('请输入学生的姓名: '))
                        elif _Num == 2:
                            _Phone = int(input('请输入学生电话: '))
                        elif _Num == 3:
                            _Company = str(input('请输入学生的公司名称: '))
                        elif _Num == 4:
                            _Address = str(input('请输入学生住址: '))
                        elif _Num == 5:
                            _Email = str(input('请输入学生Email: '))
                            for i in range(1, 4):  # 邮箱格式校验
                                if _Email.find('@') == -1:
                                    if i <= 2:
                                        print('Email必须包含@，格式输入有误，请重新输入')
                                        _Email = str(input('Email: '))
                                    else:
                                        sys.exit('Email格式输入错误次数过多，程序退出.')
                        else:
                            print('已成功退出修改学生信息菜单.')
                        _Question = input('是否需要继续修改学生信息[Yy|Nn]: ').lower()
                        if _Question == 'y':
                            pass
                        elif _Question == 'n':
                            print('修改后的学生信息如下: \nID: {}, Name: {}, Phone: {}, Company: {}, Address: {}, Email: {}.'.format(_Id, _Name, _Phone, _Company, _Address, _Email))
                            _Rebuild = '{} {} {} {} {} {}\n'.format(_Id, _Name, _Phone, _Company, _Address, _Email)
                            _Result = str(input('是否更新 {} 的学生信息[Yy|Nn]:'.format(_Id))).lower()
                            if _Result == 'n':
                                print('已取消更新学生信息.')
                                break
                            elif _Result == 'y':
                                with open(_StuInfo,'r') as fs:
                                    _Lines = fs.readlines()
                                with open(_StuInfo,'w') as fs:
                                    for _Line in _Lines:
                                        if _StuId in _Line:
                                            continue
                                        fs.write(_Line)
                                    fs.write(_Rebuild)
                                    print('该学生ID {} 信息已更新.\n'.format(_StuId))
                                    break
                            else:
                                print('输入错误.')
                                break
                if _Choose == 4:
                    with open(_StuInfo, 'r') as f:
                        for _Item in f.readlines():
                            _Id,_Name,_Phone,_Company,_Address,_Email = _Item.split()
                            _StuDist[_Id] = [_Name,_Phone,_Company,_Address,_Email]
                            if _Name == _Email.split('@')[0]:
                                sys.exit("学生姓名 \033[31;1m{}\033[0m 和Email昵称 \033[31;1m{}\033[0m 不能相同,请修改.".format(_Name, _Email))
                    print('支持精确查询学生ID,模糊查询学生姓名等其他信息.')
                    while True:
                        _Quary = str(input('请输入需要查询的学生信息: ').strip().lower())
                        if len(_Quary) < 3:
                            print('请最少输入三位学生ID.')
                            continue
                        if _Quary in _StuDist.keys():   #精确匹配学生ID
                            _QuaryInfo = ','.join(_StuDist[_Quary]).strip('\n').split(',')
                            _Name, _Phone, _Company, _Address, _Email = _QuaryInfo
                            print('ID: {}, Name: {}, Phone: {}, Company: {}, Address: {}, Email: {}.'.format(_Quary, _Name,_Phone,_Company,_Address,_Email))
                            _QuaryResult = str(input('是否退出查询[Yy|Nn):').lower())
                            if _QuaryResult == 'n':
                                pass
                            else:
                                break
                        else:
                            #模糊匹配学生其他信息.
                            _MatchCount = 0
                            for _k, _v in _StuDist.items():
                                for _Info in _v:
                                    if _Info.lower().find(_Quary) != -1:
                                        _QuaryInfo = ','.join(_v).strip('\n').split(',')
                                        _Name, _Phone, _Company, _Address, _Email = _QuaryInfo
                                        print('ID: {}, Name: {}, Phone: {}, Company: {}, Address: {}, Email: {}.'.format(_k, _Name, _Phone, _Company, _Address, _Email))
                                        _MatchCount += 1
                            print('Matched \033[31;1m%s\033[0m recodes!' % _MatchCount)
                            _QuaryResult = str(input('是否退出查询[Yy|Nn):').lower())
                            if _QuaryResult == 'n':
                                pass
                            else:
                                break
                if _Choose == 5:
                    _Quary = str(input('是否查询所有学生信息[Yy|Nn]:').lower())
                    with open(_StuInfo, 'r') as f:
                        for _Item in f.readlines():
                            _Id,_Name,_Phone,_Company,_Address,_Email = _Item.split()
                            if _Quary == 'n':
                                print('已成功取消所有学生信息查询.')
                                break
                            elif _Quary == 'y':
                                print('查询到的学生信息如下: \nID: {}, Name: {}, Phone: {}, Company: {}, Address: {}, Email: {}.\n'.format(_Id, _Name, _Phone, _Company, _Address, _Email))
                            else:
                                print('输入错误.')
                                break
                if _Choose == 6:
                    _QuaryResult = str(input('请问是否退出菜单[Yy|Nn):').lower())
                    if _QuaryResult == 'n':
                        pass
                    else:
                        sys.exit('已成功退出菜单.')