# -*- coding:utf-8 -*-
# Author:dongdong Liu
"""
for 循环是迭代循环，在Python中相当于一个通用的序列迭代器，可以遍历任何有序序列，如 str、list、tuple 等，也
可以遍历任何可迭代对象，如 dict 。
for 迭代变量 in 可迭代对象:
    代码块
每次循环，迭代变量被设置为可迭代对象的当前元素，提供给代码块使用。
"""
studentNames = ["张三", "李四", "王五"]
for name in studentNames:
    print("你叫什么名字", name)

"""
for 迭代变量 in 可迭代对象:
    代码块
else:
    代码块
当 for 循环正常执行完的情况下，执行 else 输出，如果 for 循环中执行了跳出循环的语句，比如 break ，将不执
行 else 代码块的内容，与 while - else 语句一样。
"""