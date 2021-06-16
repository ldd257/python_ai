#  Python format 格式化函数
str = "{0} Love {1}".format('I', 'Lsgogroup') # 位置参数
print(str) # I Love Lsgogroup
str = "{a} Love {b}".format(a='I', b='Lsgogroup') # 关键字参数
print(str) # I Love Lsgogroup
str = "{0} Love {b}".format('I', b='Lsgogroup') # 位置参数要在关键字参数之前
print(str) # I Love Lsgogroup
str = '{0:.2f}{1}'.format(27.658, 'GB') # 保留小数点后两位
print(str) # 27.66GB

"""
Python 字符串格式化符号
符号     描述
%c      格式化字符及其ASCII码
%s      格式化字符串，用str()方法处理对象
%r      格式化字符串，用rper()方法处理对象
%d      格式化整数
%o      格式化无符号八进制数
%x      格式化无符号十六进制数
%X      格式化无符号十六进制数（大写）
%f      格式化浮点数字，可指定小数点后的精度
%e      用科学计数法格式化浮点数
%E      作用同%e，用科学计数法格式化浮点数
%g      根据值的大小决定使用%f或%e
%G      作用同%g，根据值的大小决定使用%f或%E
"""
print('%c' % 97) # a
print('%c %c %c' % (97, 98, 99)) # a b c
print('%d + %d = %d' % (4, 5, 9)) # 4 + 5 = 9
print("我叫 %s 今年 %d 岁!" % ('小明', 10)) # 我叫 小明 今年 10 岁!
print('%o' % 10) # 12
print('%x' % 10) # a
print('%X' % 10) # A
print('%f' % 27.658) # 27.658000
print('%e' % 27.658) # 2.765800e+01
print('%E' % 27.658) # 2.765800E+01
print('%g' % 27.658) # 27.658
text = "I am %d years old." % 22
print("I said: %s." % text) # I said: I am 22 years old..
print("I said: %r." % text) # I said: 'I am 22 years old.'


"""
格式化操作符辅助指令
符号 功能
m.n m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话) - 用做左对齐
+ 在正数前面显示加号( + )
# 在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
0 显示的数字前面填充'0'而不是默认的空格
"""
print('%5.1f' % 27.658) # ' 27.7'
print('%.2e' % 27.658) # 2.77e+01
print('%10d' % 10) # ' 10'
print('%-10d' % 10) # '10 '
print('%+d' % 10) # +10
print('%#o' % 10) # 0o12
print('%#x' % 108) # 0x6c
print('%010d' % 5) # 0000000005