# -*- coding:utf-8 -*-
# Author:dongdong Liu
"""
while 语句最基本的形式包括一个位于顶部的布尔表达式，一个或多个属于 while 代码块的缩进语句。
while 布尔表达式:
    代码块
while 循环的代码块会一直循环执行，直到布尔表达式的值为布尔假。
如果布尔表达式不带有 <、>、==、！=、in、not in 等运算符，仅仅给出数值之类的条件，也是可以的。当 while 后写
入一个非零整数时，视为真值，执行循环体；写入 0 时，视为假值，不执行循环体。也可以写入 str、list 或任何序
列，长度非零则视为真值，执行循环体；否则视为假值，不执行循环体。
"""
i = 1
while i <= 3:
    print("我要循环三次", i)
    i += 1


"""
while 布尔表达式:
    代码块
else:
    正常循环结束代码块
当 while 循环正常执行完的情况下，执行 else 输出，如果 while 循环中执行了跳出循环的语句，比如 break ，将不执
行 else 代码块的内容。
"""
i = 1
while i <= 3:
    print("我要循环三次", i)
    i += 1
else:
    print("我循环结束了")