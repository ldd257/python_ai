"""
Python 的函数具有非常灵活多样的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。从简到繁的参数形态
如下：
1. 位置参数 (positional argument)
2. 默认参数 (default argument)
3. 可变参数 (variable argument)
4. 关键字参数 (keyword argument)
5. 命名关键字参数 (name keyword argument)
6. 参数组合
"""

"""
1. 位置参数
def functionname(arg1):
 "函数_文档字符串"
 function_suite
 return [expression]
 
 arg1 - 位置参数 ，这些参数在调用函数 (call function) 时位置要固定。
"""


"""
2. 默认参数
def functionname(arg1, arg2=v):
 "函数_文档字符串"
 function_suite
 return [expression]
 
 1. arg2 = v - 默认参数 = 默认值，调用函数时，默认参数的值如果没有传入，则被认为是默认值。
2. 默认参数一定要放在位置参数 后面，不然程序会报错

 Python 允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
"""
def printinfo(name, age=8):
    print('Name:{0},Age:{1}'.format(name, age))
printinfo('小马') # Name:小马,Age:8
printinfo('小马', 10) # Name:小马,Age:10

"""
3. 可变参数
顾名思义，可变参数就是传入的参数个数是可变的，可以是 0, 1, 2 到任意个，是不定长的参数。
def functionname(arg1, arg2=v, *args):
 "函数_文档字符串"
 function_suite
 return [expression]

1. *args - 可变参数，可以是从零个到任意个，自动组装成元组。
2. 加了星号（*）的变量名会存放所有未命名的变量参数。
"""
def printinfo(arg1, *args):
 print(arg1)
 for var in args:
    print(var)
printinfo(10) # 10
printinfo(70, 60, 50)
# 70
# 60
# 50

"""
4.关键字参数
def functionname(arg1, arg2=v, *args, **kw):
 "函数_文档字符串"
 function_suite
 return [expression]
 
  **kw - 关键字参数，可以是从零个到任意个，自动组装成字典。

「可变参数」和「关键字参数」的同异总结如下：
1. 可变参数允许传入零个到任意个参数，它们在函数调用时自动组装为一个元组 (tuple)。
2. 关键字参数允许传入零个到任意个参数，它们在函数内部自动组装为一个字典 (dict)。
"""
def printinfo(arg1, *args, **kwargs):
    print(arg1)
    print(args)
    print(kwargs)
printinfo(70, 60, 50)
# 70
# (60, 50)
# {}
printinfo(70, 60, 50, a=1, b=2)
# 70
# (60, 50)
# {'a': 1, 'b': 2}

"""
5.命名关键字参数
def functionname(arg1, arg2=v, *args, *, nkw, **kw):
 "函数_文档字符串"
 function_suite
 return [expression]
 
1. *, nkw - 命名关键字参数，用户想要输入的关键字参数，定义方式是在nkw 前面加个分隔符 *。
2. 如果要限制关键字参数的名字，就可以用「命名关键字参数」
3. 使用命名关键字参数时，要特别注意不能缺少参数名。

1. 没有写参数名 nwk ，因此 10 被当成「位置参数」，而原函数只有 1 个位置函数，现在调用了 2 个，因此程序会报
错。
"""
def printinfo(arg1, *, nkw, **kwargs):
 print(arg1)
 print(nkw)
 print(kwargs)
printinfo(70, nkw=10, a=1, b=2)
# 70
# 10
# {'a': 1, 'b': 2}
printinfo(70, 10, a=1, b=2)
# TypeError: printinfo() takes 1 positional argument but 2 were given


"""
6. 参数组合 在 Python 中定义函数，可以用位置参数、默认参数、可变参数、命名关键字参数和关键字参数，这 5 种参数中的 4 个都
可以一起使用，但是注意，参数定义的顺序必须是：
1. 位置参数、默认参数、可变参数和关键字参数。
2. 位置参数、默认参数、命名关键字参数和关键字参数。
要注意定义可变参数和关键字参数的语法：
1. *args 是可变参数， args 接收的是一个 tuple
2. **kw 是关键字参数， kw 接收的是一个 dict
命名关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。定义命名关键字参数不要忘了写分隔符
* ，否则定义的是位置参数。
警告：虽然可以组合多达 5 种参数，但不要同时使用太多的组合，否则函数很难懂。
"""