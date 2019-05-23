<!--ts-->
   * [作业](#作业)
      * [1，字符串方法 和 列表方法](#1字符串方法-和-列表方法)
      * [2，用户管理系统](#2用户管理系统)
      * [3，冒泡排序](#3冒泡排序)

<!-- Added by: root, at: Thu May 23 01:24:58 CST 2019 -->

<!--te-->

# 作业

## 1，字符串方法 和 列表方法 
> 写成docstring中文文档README.md


>>> dir(str)  
### .count

子串搜索

返回字符串S中子串sub出现的次数，可以指定从哪里开始计算(start)以及计算到哪里结束(end)，索引从0开始计算，不包括end边界。

> S.count(sub[, start[, end]])




.startswith
.endswith
.find
.format
.index
.isdigit
.islower
.isupper
.join
.ljust
.lower
.lstrip
.replace
.rjust
.split
.strip
.upper


>>> dir(list)    
.append
.count
.extend
.index
.insert
.pop
.remove
.reverse
.sort


## 2，用户管理系统
```bash
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add
    3.2 删 delete
    3.3 改 update
    3.4 查 list
    3.5 搜 find
3. 格式化输出   
```

```shell
[root@51reboot lesson02]# python homework_01_user_mgt_system.py
Please input your username: 11
Please input your password: 11
 username or password error,you have 5 times to input 
Please input your username: 11
Please input your password: 11
 username or password error,you have 4 times to input 
Please input your username: 11
Please input your password: 11
 username or password error,you have 3 times to input 
Please input your username: admin
Please input your password: 123456
Please input the action and info: add xiaoming 20 18212345678 1234@qq.com
add 'xiaoming 20 18212345678 1234@qq.com' succeed
Please input the action and info: add xiaohong 18 18233335678 6666@qq.com
add 'xiaohong 18 18233335678 6666@qq.com' succeed
Please input the action and info: add xiaohong 18 18233335678 6666@qq.com
'xiaohong 18 18233335678 6666@qq.com' is already added
Please input the action and info: find xiaohong
--------------------------------------------------------
|name       |age |Tel           |Email               
--------------------------------------------------------
|xiaohong   |18  |18233335678   |6666@qq.com         
Please input the action and info: update xiaoming set age = 22
Please input the action and info: find xiaoming
--------------------------------------------------------
|name       |age |Tel           |Email               
--------------------------------------------------------
|xiaoming   |22  |18212345678   |1234@qq.com         
Please input the action and info: update xiaoming set age=23          
Please input the action and info: find xiaoming
--------------------------------------------------------
|name       |age |Tel           |Email               
--------------------------------------------------------
|xiaoming   |23  |18212345678   |1234@qq.com         
Please input the action and info: list
--------------------------------------------------------
|name       |age |Tel           |Email               
--------------------------------------------------------
|xiaoming   |23  |18212345678   |1234@qq.com         
--------------------------------------------------------
|xiaohong   |18  |18233335678   |6666@qq.com         
Please input the action and info: 
```


## 3，冒泡排序
```bash
需求：
- [3, 7, 2, 5, 20, 11]

将列表通过冒泡排序的方式实现排序。

```

```shell
[root@51reboot lesson02]# ./bubble_sort.py  
第1次比较后的数组：
[3, 2, 5, 7, 11, 20]
第2次比较后的数组：
[2, 3, 5, 7, 11, 20]
第3次比较后的数组：
[2, 3, 5, 7, 11, 20]
第4次比较后的数组：
[2, 3, 5, 7, 11, 20]
第5次比较后的数组：
[2, 3, 5, 7, 11, 20]
```
