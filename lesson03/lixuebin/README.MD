# 李学彬第三次作业

## 功能实现:

1. 将列表转换为字典
2. 分页 --> 根据page和pagesize 进行分页并优雅输出 --> 对分页数量进行判断,超出后提示
3. 持久化数据 --> 默认在数据更改后会自动持久化, 导入数据和清空数据会询问是否永久保存
4. 异常处理 --> 对整个程序的所有操作异常处理
5. 优雅格式化输出 --> 从登陆后的命令提示界面到列表查询,到分页,全部优雅格式化输出
6. 支持导出数据到csv --> 支持自定义/默认路径和文件名 --> 导出后判断文件是否存在 --> 提示成功或失败
7. 记录登陆日志 --> 登陆成功 --> log/login.log  登陆失败 --> log/loginFail.log
8. 记录操作日志 --> 对add, update, delete, clear, export, import操作进行记录
9. 统计用户数量
10. 清空用户 --> 临时清空 --> 可以reload加载 --> 询问是否永久清空 --> 直接修改文件永久清空
11. 支持从cvs中导入数据 --> 文件存在 --> 文件格式校验 --> 重复数据校验

## 用法描述和命令

| Serial | Description | Command |
| :------: | ----------- | ------- |
| 1 | Add user info | add username age tel email |
| 2 | Delete user | delete username |
| 3 | Update user info | update username set (age\|tel\|email) = new value          |
| 4 | Find user info | find username |
| 5 | Show tables | list |
| 6 | Pagination display | display page 1 pagesize 5 |
| 7 | Count of users | count |
| 8 | Clear users table | clear |
| 9 | Reload when temporarily emptied | reload |
| 10 | Export csv file | export [path/filename].Default "csv/UserData+unixtime.csv" |
| 11 | From csv file import data | import "path/filename" |

```
+--------+---------------------------------+------------------------------------------------------------+
| Serial | Description                     | Command                                                    |
+--------+---------------------------------+------------------------------------------------------------+
|   1    | Add user info                   | add username age tel email.                                |
|   2    | Delete user                     | delete username.                                           |
|   3    | Update user info                | update username set (age|tel|email) = new info.            |
|   4    | Find user info                  | find username.                                             |
|   5    | Show tables                     | list.                                                      |
|   6    | Pagination display              | display page 1 pagesize 5.                                 |
|   7    | Count of users                  | count.                                                     |
|   8    | Clear users table               | clear.                                                     |
|   9    | Reload when temporarily emptied | reload.                                                    |
|   10   | Export csv file                 | export [path/filename].Default "csv/UserData+unixtime.csv" |
|   11   | From csv file import data       | import "path/filename"                                     |
+--------+---------------------------------+------------------------------------------------------------+

```

