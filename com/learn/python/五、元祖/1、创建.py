"""
元组
「元组」定义语法为： (元素1, 元素2, ..., 元素n)
1. 小括号把所有元素绑在一起
2. 逗号将每个元素一一分开
"""

"""
1. Python 的元组与列表类似，不同之处在于tuple被创建后就不能对其进行修改，类似字符串。
2. 元组使用小括号，列表使用方括号。
"""
t1 = (1, 10.31, 'python')
t2 = 1, 10.31, 'python'
print(t1, type(t1))
# (1, 10.31, 'python') <class 'tuple'>
print(t2, type(t2))
# (1, 10.31, 'python') <class 'tuple'>

tuple1 = (1, 2, 3, 4, 5, 6, 7, 8)
print(tuple1[1]) # 2
print(tuple1[5:]) # (6, 7, 8)
print(tuple1[:5]) # (1, 2, 3, 4, 5)
tuple2 = tuple1[:]
print(tuple2) # (1, 2, 3, 4, 5, 6, 7, 8)

"""
1. 创建元组可以用小括号 ()，也可以什么都不用，为了可读性，建议还是用 ()。 
2. 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
"""
temp = (1)
print(type(temp)) # <class 'int'>
temp = 2, 3, 4, 5
print(type(temp)) # <class 'tuple'>
temp = []
print(type(temp)) # <class 'list'>
temp = ()
print(type(temp)) # <class 'tuple'>
temp = (1,)
print(type(temp)) # <class 'tuple'>


"""
元组有不可更改 (immutable) 的性质，因此不能直接给元组的元素赋值，但是只要元组中的元素可更改 (mutable)，那么我
们可以直接更改其元素，注意这跟赋值其元素不同。
"""
week = ('Monday', 'Tuesday', 'Thursday', 'Friday')
week = week[:2] + ('Wednesday',) + week[2:]
print(week) # ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
t1 = (1, 2, 3, [4, 5, 6])
print(t1) # (1, 2, 3, [4, 5, 6])
t1[3][0] = 9
print(t1) # (1, 2, 3, [9, 5, 6])
