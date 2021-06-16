"""
字符串的切片与拼接
1. 类似于元组具有不可修改性
2. 从 0 开始 (和 C 一样)
3. 切片通常写成 start:end 这种形式，包括「 start 索引」对应的元素，不包括「 end 索引」对应的元素。
4. 索引值可正可负，正索引从 0 开始，从左往右；负索引从 -1 开始，从右往左。使用负数索引时，会从最后一个元素
开始计数。最后一个元素的位置编号是 -1。
"""
str1 = 'I Love LsgoGroup'
print(str1[:6]) # I Love
print(str1[5]) # e
print(str1[:6] + " 插入的字符串 " + str1[6:])
# I Love 插入的字符串 LsgoGroup


"""
字符串的常用内置方法
1. capitalize() 将字符串的第一个字符转换为大写。
2. lower() 转换字符串中所有大写字符为小写。
3. upper() 转换字符串中的小写字母为大写。
4. swapcase() 将字符串中大写转换为小写，小写转换为大写。
5. count(str, beg= 0,end=len(string)) 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定
范围内 str 出现的次数。
6. endswith(suffix, beg=0, end=len(string)) 检查字符串是否以指定子字符串 suffix 结束，如果是，返回
True,否则返回 False。如果 beg 和 end 指定值，则在指定范围内检查。
7. startswith(substr, beg=0,end=len(string)) 检查字符串是否以指定子字符串 substr 开头，如果是，返回
True，否则返回 False。如果 beg 和 end 指定值，则在指定范围内检查。
8. find(str, beg=0, end=len(string)) 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是
否包含在指定范围内，如果包含，返回开始的索引值，否则返回 -1。
9. rfind(str, beg=0,end=len(string)) 类似于 find() 函数，不过是从右边开始查找。
10. isnumeric() 如果字符串中只包含数字字符，则返回 True，否则返回 False。
11. ljust(width[, fillchar]) 返回一个原字符串左对齐，并使用 fillchar （默认空格）填充至长度 width 的新字
符串。
12. rjust(width[, fillchar]) 返回一个原字符串右对齐，并使用 fillchar （默认空格）填充至长度 width 的新字
符串。
"""
str2 = 'xiaoxie'
print(str2.capitalize()) # Xiaoxie

str2 = "DAXIExiaoxie"
print(str2.lower()) # daxiexiaoxie
print(str2.upper()) # DAXIEXIAOXIE
print(str2.swapcase()) # daxieXIAOXIE

str2 = "DAXIExiaoxie"
print(str2.count('xi')) # 2

str2 = "DAXIExiaoxie"
print(str2.endswith('ie')) # True
print(str2.endswith('xi')) # False
print(str2.startswith('Da')) # False
print(str2.startswith('DA')) # True

str2 = "DAXIExiaoxie"
print(str2.find('xi')) # 5
print(str2.find('ix')) # -1
print(str2.rfind('xi')) # 9

str3 = '12345'
print(str3.isnumeric()) # True
str3 += 'a'
print(str3.isnumeric()) # False

str4 = '1101'
print(str4.ljust(8, '0')) # 11010000
print(str4.rjust(8, '0')) # 00001101


"""
13. lstrip([chars]) 截掉字符串左边的空格或指定字符。
14. rstrip([chars]) 删除字符串末尾的空格或指定字符。
15. strip([chars]) 在字符串上执行 lstrip() 和 rstrip() 。
"""
str5 = ' I Love LsgoGroup '
print(str5.lstrip()) # 'I Love LsgoGroup '
print(str5.lstrip().strip('I')) # ' Love LsgoGroup '
print(str5.rstrip()) # ' I Love LsgoGroup'
print(str5.strip()) # 'I Love LsgoGroup'
print(str5.strip().strip('p')) # 'I Love LsgoGrou'

"""
16. partition(sub) 找到子字符串sub，把字符串分为一个三元组 (pre_sub,sub,fol_sub) ，如果字符串中不包含
sub则返回 ('原字符串','','') 。
17. rpartition(sub) 类似于 partition() 方法，不过是从右边开始查找
"""
str5 = ' I Love LsgoGroup '
print(str5.strip().partition('o')) # ('I L', 'o', 've LsgoGroup')
print(str5.strip().partition('m')) # ('I Love LsgoGroup', '', '')
print(str5.strip().rpartition('o')) # ('I Love LsgoGr', 'o', 'up')

"""
18. replace(old, new [, max]) 把 将字符串中的 old 替换成 new ，如果 max 指定，则替换不超过 max 次。
19. split(str="", num) 不带参数默认是以空格为分隔符切片字符串，如果 num 参数有设置，则仅分隔 num 个子字符
串，返回切片后的子字符串拼接的列表。
20. splitlines([keepends]) 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为
False，不包含换行符，如果为 True，则保留换行符。
"""
str5 = ' I Love LsgoGroup '
print(str5.strip().replace('I', 'We')) # We Love LsgoGroup

str5 = ' I Love LsgoGroup '
print(str5.strip().split()) # ['I', 'Love', 'LsgoGroup']
print(str5.strip().split('o')) # ['I L', 've Lsg', 'Gr', 'up']

str6 = 'I \n Love \n LsgoGroup'
print(str6.splitlines()) # ['I ', ' Love ', ' LsgoGroup']
print(str6.splitlines(True)) # ['I \n', ' Love \n', ' LsgoGroup']

"""
21. maketrans(intab, outtab) 创建字符映射的转换表，第一个参数是字符串，表示需要转换的字符，第二个参数也
是字符串表示转换的目标。
22. translate(table, deletechars="") 根据参数 table 给出的表，转换字符串的字符，要过滤掉的字符放
到 deletechars 参数中。
"""
str = 'this is string example....wow!!!'
intab = 'aeiou'
outtab = '12345'
trantab = str.maketrans(intab, outtab)
print(trantab) # {97: 49, 111: 52, 117: 53, 101: 50, 105: 51}
print(str.translate(trantab)) # th3s 3s str3ng 2x1mpl2....w4w!!!