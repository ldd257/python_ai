"""
if expression:
    expr_true_suite
elif expression:
    expr_true_suite
else:
    expr_true_suite

1. if 语句的 expr_true_suite 代码块只有当条件表达式 expression 结果为真时才执行，否则将继续执行紧跟在该
代码块后面的语句。
2. 单个 if 语句中的 expression 条件表达式可以通过布尔操作符 and ， or 和 not 实现多重条件判断。
"""
age = 27
if age > 30:
    print("年龄大于三十")
else:
    print("年龄小于三十")


"""
if 语句支持嵌套，即在一个 if 语句中嵌入另一个 if 语句，从而构成不同层次的选择结构。Python 使用缩进而不是大括
号来标记代码块边界，因此要特别注意 else 的悬挂问题。
"""
hi = 6
if hi > 2:
    if hi > 7:
        print('好棒!好棒!')
else:
    print('切~')


"""
assert 这个关键词我们称之为“断言”，当这个关键词后边的条件为 False 时，程序自动崩溃并抛
出 AssertionError 的异常。
"""
assert 2>3