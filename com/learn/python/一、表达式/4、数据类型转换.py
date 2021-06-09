"""
数值类型
int     整型      -876, 10
float   浮点型     3.149, 11.11
bool    布尔型     True, False
"""
# 0. 获取类型信息
"""
获取类型信息 type(object)  isinstance(object, classinfo)
1. type() 不会认为子类是一种父类类型，不考虑继承关系。
2. isinstance() 会认为子类是一种父类类型，考虑继承关系。
"""

# 1. 整型
age = 27
print(type(age))
# <class 'int'>

# 2. 浮点型
price = 3.2
print(type(price))
# <class 'float'>

# 3. 布尔型
on = True
print(type(on))
# <class 'bool'>

"""
类型转换 即通过数值类型所对应的类去实现转换
类型转换
1. 转换为整型 int(x, base=10)
2. 转换为字符串 str(object='')
3. 转换为浮点型 float(x)
"""
print(int(True)) # 1
print(float(1)) # 1.0
print(bool(1)) # True
'''
除了直接给变量赋值 True 和 False ，还可以用 bool(X) 来创建变量，其中 X 可以是
1. 基本类型：整型、浮点型、布尔型
2. 容器类型：字符、元组、列表、字典和集合

确定 bool(X) 的值是 True 还是 False ，就看 X 是不是空，空的话就是 False ，不空的话就是 True 。 1. 对于数值变量， 0 , 0.0 都可认为是空的。
2. 对于容器变量，里面没元素就是空的。
'''