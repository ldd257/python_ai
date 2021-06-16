"""
字符串的定义
1. Python 中字符串被定义为引号之间的字符集合。
2. Python 支持使用成对的 单引号 或 双引号。
"""
t1 = 'i love Python!'
print(t1, type(t1))
# i love Python! <class 'str'>
t2 = "I love Python!"
print(t2, type(t2))
# I love Python! <class 'str'>
print(5 + 8) # 13
print('5' + '8') # 58

"""
如果字符串中需要出现单引号或双引号，可以使用转义符号 \ 对字符串中的符号进行转义。
1. Python 的常用转义字符
转义字符 描述
\\ 反斜杠符号
\' 单引号
\" 双引号
\n 换行
\t 横向制表符(TAB)
\r 回车
"""
print('let\'s go') # let's go
print("let's go") # let's go

# 2.  原始字符串只需要在字符串前边加一个英文字母 r 即可。
print(r'C:\Program Files\Intel\Wifi\Help')
# C:\Program Files\Intel\Wifi\Help

#  python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)

