# -*- coding:utf-8 -*-
# author: lyl

from django import template

register = template.Library()

@register.filter(name='orderfile_name')
def orderfile_name(file_path):
    """
    截取上传文件的文件名
    上传文件数据库中存放的格式：orderfiles/2019/06/aa.txt
    最终需要的格式：aa.txt
    """
    # print(file_path)   # orderfiles/2019/06/aa.txt
    file_name = str(file_path).split('/')[-1]   # aa.txt
    return file_name

@register.filter(name='userlist_str2')
def userlist_str2(user_list):
    """
    将用户列表转换为str
    """
    if len(user_list) < 3:
        return ' '.join([user.name_cn for user in user_list])
    else:
        return '%s ...' % ' '.join([user.name_cn for user in user_list[0:2]])



@register.filter(name='perm_str2')
def perm_str2(perm_list):
    """
    将用户或者租的权限列表转换为str
    """
    if len(perm_list) < 3:
        return ' '.join([perm.codename for perm in perm_list])
    else:
        return '%s ...' % ' '.join([perm.codename for perm in perm_list[0:2]])