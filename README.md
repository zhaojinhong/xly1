# xly1

## 1. 命令行添加代码

- Windwos 或 Mac:
```
# 第一次使用

git clone https://github.com/51reboot/xly1.git
cd xly1/lesson01/
mkdir monkey                            # 添加自已名称目录， 用拼音表示
echo "print("hello world")" >> monkey/zuoye.py
git add monkey/zuoye.py
git status     # 查看当前github作业提交状态
git commit -m "add monkey/zuoye.py"     # 提交代码到本地仓库
git pull			        # 防止冲突,每次push之前先pull
git push -u origin master               # 提交代码到远程仓库

# 后面写好作业后，只需要下面三行即可
git add .
git commit -m "modify monkey/zuoye.py"	# 引号内为本次提交的描述,请自行更改
git pull			        # 防止冲突,每次push之前先pull
git push 
```

## 2. vagrant虚拟机如果报错往下看:

> 因虚拟机yum源默认版本为git-1.7.1, 所以会导致报错**

  - 第一步:

    `yum -y install http://opensource.wandisco.com/centos/6/git/x86_64/git-2.2.1-1.WANdisco.232.x86_64.rpm`

  - 第二步:

    `yum update -y nss curl libcurl`

  - 然后在执行上面操作

    注意:   如果你开了翻墙软件并且不是日本节点,请先关闭翻墙软件在进行升级.
