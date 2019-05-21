#字符串方法 和 列表方法
## 写成docstring中文文档README.md

## 字符串方法
> dir(str)  

###  count
> count(str, beg= 0,end=len(string))
> 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数

###  startswith
startswith(substr, beg=0,end=len(string))
检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。

###  endswith
ndswith(suffix, beg=0, end=len(string))
检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False###  

###  find
find(str, beg=0, end=len(string))
检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1

###  format
Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。

###  index
index(str, beg=0, end=len(string))
跟find()方法一样，只不过如果str不在字符串中会报一个异常

###  isdigit
如果字符串只包含数字则返回 True 否则返回 False

###  islower
如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False

###  isupper
如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False

###  join
join(seq)
以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串

###  ljust
ljust(width[, fillchar])
返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。

###  lower
转换字符串中所有大写字符为小写

###  lstrip
截掉字符串左边的空格或指定字符。

###  replace
replace(old, new [, max])
把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。

###  rjust
rjust(width,[, fillchar])
返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串

###  split
split(str="", num=string.count(str))
num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串

###  strip	
strip([chars])
在字符串上执行 lstrip()和 rstrip()

###  upper
转换字符串中的小写字母为大写


## dir(list) 
   
###  append
list.append(obj)
在列表末尾添加新的对象

###  count
list.count(obj)
统计某个元素在列表中出现的次数

###  extend
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）

###  index
从列表中找出某个值第一个匹配项的索引位置

###  insert
将对象插入列表

###  pop
list.pop([index=-1])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

###  remove
移除列表中某个值的第一个匹配项

###  reverse
反向列表中元素

###  sort
list.sort( key=None, reverse=False)
对原列表进行排序

