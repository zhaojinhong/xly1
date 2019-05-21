##笔记地址
https://gjwlinux.github.io/archives/
##冒泡排序测试
```
gjwdeMacBook-Pro:gaojiawei gjw$ python3.6 hw_sort.py 
[1, 2, 3, 5, 6, 7, 9]
```
##用户管理使用
###登录测试,6次退出
```
gjwdeMacBook-Pro:gaojiawei gjw$ python3 hw_userinfo.py 
Please input your username: 1
Please input your password: 1
Username or password error.
Please input your username: 1
Please input your password: 1
Username or password error.
Please input your username: 1
Please input your password: 1
Username or password error.
Please input your username: 1
Please input your password: 1
Username or password error.
Please input your username: 1
Please input your password: 1
Username or password error.
Please input your username: 1
Please input your password: 1
Username or password error.
```
###增加用户add，名字相同提示
```
gjwdeMacBook-Pro:gaojiawei gjw$ python3 hw_userinfo.py 
Please input your username: 51reboot
Please input your password: 123456
Login successful
Please input your operation: add gjw 11 111 111
Add gjw succ.
Please input your operation: add gjw1 11 111 111
Add gjw1 succ.
Please input your operation: add gjw1 11 111 111
User already exists
```
###删除查询所有delete list，查询如果是空提示空
```
Please input your operation: delete gjw1     
Del gjw1 succ.
username age tel email	
--------------------------------------------------
gjw 11 111 111	
--------------------------------------------------
Please input your operation: delete gjw
Del gjw succ.
username age tel email	
--------------------------------------------------
Please input your operation: list
User information is empty.
Please input your operation: add gjw 18 177 177@qq.com
Add gjw succ.
Please input your operation: list
username age tel email	
--------------------------------------------------
gjw 18 177 177@qq.com	
--------------------------------------------------

```
###修改逻辑，可通过set name,age,tel,email,修改
```
Please input your operation: list
username age tel email	
--------------------------------------------------
gjw 18 177 177@qq.com	
--------------------------------------------------
gjw1 18 177 177@qq.com	
--------------------------------------------------
Please input your operation: update gjw1 set age = 19
Update gjw1 succ.
--------------------------------------------------
username age tel email	
--------------------------------------------------
gjw 18 177 177@qq.com	
--------------------------------------------------
gjw1 19 177 177@qq.com	
--------------------------------------------------
Please input your operation: update gjw1 set tel = 188
Update gjw1 succ.
--------------------------------------------------
username age tel email	
--------------------------------------------------
gjw 18 177 177@qq.com	
--------------------------------------------------
gjw1 19 188 177@qq.com	
--------------------------------------------------
Please input your operation: update gjw1 set email = 188@qq.com
Update gjw1 succ.
--------------------------------------------------
username age tel email	
--------------------------------------------------
gjw 18 177 177@qq.com	
--------------------------------------------------
gjw1 19 188 188@qq.com	
--------------------------------------------------
Please input your operation: update gjw1 set name = gjw
User already exists
--------------------------------------------------
username age tel email	
--------------------------------------------------
gjw 18 177 177@qq.com	
--------------------------------------------------
gjw1 19 188 188@qq.com	
--------------------------------------------------
Please input your operation: update gjw1 set name = mk
Update gjw1 succ.
--------------------------------------------------
username age tel email	
--------------------------------------------------
gjw 18 177 177@qq.com	
--------------------------------------------------
mk 19 188 188@qq.com	
--------------------------------------------------
Please input your operation: exit
by
```
