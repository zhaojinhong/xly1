# 字符串方法  
### count方法:
用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置  
```python
str.count(sub, start= 0,end=len(string))
```
#### option:
* sub -- 搜索的子字符串
* start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
* end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。
***

### startswith:
用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查。  
```python
str.startswith(substr, beg=0,end=len(string));
```
#### option:  
* str -- 检测的字符串。
* substr -- 指定的子字符串。
* strbeg -- 可选参数用于设置字符串检测的起始位置。  
* strend -- 可选参数用于设置字符串检测的结束位置。
***

### endswith:
用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。可选参数"start"与"end"为检索字符串的开始与结束位置。
```python
str.endswith(suffix[, start[, end]])
```
#### option:  
* suffix -- 该参数可以是一个字符串或者是一个元素。  
* start -- 字符串中的开始位置。  
* end -- 字符中结束位置。  
***

### find:
检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果指定范围内包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。
```python
str.find(str, beg=0, end=len(string))
```
#### option:
* str -- 指定检索的字符串
* beg -- 开始索引，默认为0。
* end -- 结束索引，默认为字符串的长度
***

### format:
增强了字符串格式化的功能。非常灵活，可指定位置，可不指定位置，可通过索引、字典设置参数
```python
"{} xxx".format("abc")
```

***
### index:
检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
```python
str.index(str, beg=0, end=len(string))
```

#### option:
* str -- 指定检索的字符串
* beg -- 开始索引，默认为0。
* end -- 结束索引，默认为字符串的长度。
***

### isdigit:
检测字符串是否只由数字组成，返回True or False
```python
str.isdigit()
```

#### option:
无

-------------------------------------------------
### islower:
检测字符串是否由小写字母组成，返回True，只要字符串中包含一个大写字母都返回False
```python
str.islower()
```

#### option:
无
***

### isupper：
检测字符串是否由大写字母组成，返回True，只要字符串中包含一个小写字母都返回False
```python
str.isupper()
```

#### option:
无
***

### join:
用于将序列中的元素以指定的字符连接生成一个新的字符串。返回通过指定字符连接序列中元素后生成的新字符串。
```python
str.join(sequence)
```

#### option:
* sequence -- 要连接的元素序列

***

### ljust:
返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
```python
str.ljust(width[, fillchar])
```

#### option:
* width -- 指定字符串长度。
* fillchar -- 填充字符，默认为空格。
***

### lower:
转换字符串中所有大写字符为小写。返回转换后生成的字符串
```python
str.lower()
```

#### option:
无
***

### lstrip:
删除字符串左边的空格或指定字符。返回删除后生成的新字符串
```python
str.lstrip([chars])
```

#### option:
* chars --指定删除的字符
***

####replace:
把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。返回替换后的字符串
```python
str.replace(old, new[, max])
```

#### option:
* old -- 将被替换的子字符串。
* new -- 新字符串，用于替换old子字符串。
* max -- 可选字符串, 替换不超过 max 次
***

####rjust:
返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串。
```python
str.rjust(width[, fillchar])
```

#### option:
* width -- 指定填充指定字符后中字符串的总长度.
* fillchar -- 填充的字符，默认为空格。
***

### split:
通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num+1 个子字符串。返回分割后的字符串列表
```python
str.split(str="", num=string.count(str))
```

#### option:
* str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
* num -- 分割次数。默认为 -1, 即分隔所有。

***

### strip:
清除字符串左右两边的空格，等同于lstrip和rstrip同时执行。返回已清除的新字符串
```python
str.strip([chars])
```

#### option:
* chars -- 移除字符串头尾指定的字符序列。
***

### upper:
将字符串中的小写字母转为大写字母。返回小写字母转为大写字母的字符串。

```python
str.upper()
```

#### option:
无

***


