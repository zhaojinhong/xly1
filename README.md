# xly1


# Reboot 训练营第一期作业项目

# git提交千万不要用-f参数，遇到报错可以问、
# git提交千万不要用-f参数，遇到报错可以问、
# git提交千万不要用-f参数，遇到报错可以问、

## 不要删除别人的代码！


## 目录结果

* 01：第一次作业提交的目录
    - monkey  用自己的名字新建文件间
        + zuoye.py 作业的代码文件
    - nick nick的目录
        + zuoye.py 作业代码文件


## 1.桌面软件添加代码（推荐初学者）


[详细说明](https://github.com/shengxinjing/my_blog/issues/4)



## 2.命令行添加代码

- windwos或mac:
```
第一次使用
git clone https://github.com/51reboot/xly1.git
cd xly1/lesson01/
mkdir monkey 
echo  print 123 >> monkey/zuoye.py
git add .
git commit -m "first commit:joy:"
git pull								# 防止冲突,每次push之前先pull
git push

后面写好作业后，只需要下面三行即可
git add .
git commit -m "first commit"						# 引号内为本次提交的描述,请自行更改
git pull								# 防止冲突,每次push之前先pull
git push 
```

- vagrant虚拟机如上,如果报错往下看:

  **因虚拟机yum源默认版本为git-1.7.1,所以会导致报错**

  - 第一步:

    `yum -y install http://opensource.wandisco.com/centos/6/git/x86_64/git-2.2.1-1.WANdisco.232.x86_64.rpm`

  - 第二步:

    `yum update -y nss curl libcurl`

  - 然后在执行上面操作

    注意:   如果你开了翻墙软件并且不是日本节点,请先关闭翻墙软件在进行升级.
