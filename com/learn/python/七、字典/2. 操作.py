# 创建和访问字典
brand = ['李宁', '耐克', '阿迪达斯']
slogan = ['一切皆有可能', 'Just do it', 'Impossible is nothing']
print('耐克的口号是:', slogan[brand.index('耐克')])
# 耐克的口号是: Just do it
dic = {'李宁': '一切皆有可能', '耐克': 'Just do it', '阿迪达斯': 'Impossible is nothing'}
print('耐克的口号是:', dic['耐克'])
# 耐克的口号是: Just do it

"""
通过字符串或数值作为 key 来创建字典。
注意：如果我们取的键在字典中不存在，会直接报错 KeyError 。
"""
dic1 = {1: 'one', 2: 'two', 3: 'three'}
print(dic1) # {1: 'one', 2: 'two', 3: 'three'}
print(dic1[1]) # one
print(dic1[4]) # KeyError: 4

"""
通过构造函数 dict 来创建字典。
1. dict() -> 创建一个空的字典。
【例子】通过 key 直接把数据放入字典中，但一个 key 只能对应一个 value ，多次对一个 key 放入 value ，后面的值
会把前面的值冲掉
"""
dic = dict()
dic['a'] = 1
dic['b'] = 2
dic['c'] = 3
print(dic)
# {'a': 1, 'b': 2, 'c': 3}
dic['a'] = 11
print(dic)
# {'a': 11, 'b': 2, 'c': 3}

#  dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs
dic1 = dict([('apple', 4139), ('peach', 4127), ('cherry', 4098)])
print(dic1) # {'cherry': 4098, 'apple': 4139, 'peach': 4127}
dic2 = dict((('apple', 4139), ('peach', 4127), ('cherry', 4098)))
print(dic2) # {'peach': 4127, 'cherry': 4098, 'apple': 4139}

#  dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2)
# 【例子】这种情况下，键只能为字符串类型，并且创建的时候字符串不能加引号，加上就会直接报语法错误。
dic = dict(name='Tom', age=10)
print(dic) # {'name': 'Tom', 'age': 10}
print(type(dic)) # <class 'dict'>