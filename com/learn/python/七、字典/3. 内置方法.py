"""
字典的内置方法
1. dict.fromkeys(seq[, value]) 用于创建一个新字典，以序列 seq 中元素做字典的键， value 为字典所有键对应的初始值。
2. dict.keys() 返回一个可迭代对象，可以使用 list() 来转换为列表，列表为字典中的所有键。
3. dict.values() 返回一个迭代器，可以使用 list() 来转换为列表，列表为字典中的所有值。
4. dict.items() 以列表返回可遍历的 (键, 值) 元组数组。
"""
seq = ('name', 'age', 'sex')
dic1 = dict.fromkeys(seq)
print("新的字典为 : %s" % str(dic1))
# 新的字典为 : {'name': None, 'age': None, 'sex': None}
dic2 = dict.fromkeys(seq, 10)
print("新的字典为 : %s" % str(dic2))
# 新的字典为 : {'name': 10, 'age': 10, 'sex': 10}

dic = {'Name': 'lsgogroup', 'Age': 7}
print(dic.keys()) # dict_keys(['Name', 'Age'])
lst = list(dic.keys()) # 转换为列表
print(lst) # ['Name', 'Age']

dic = {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}
print("字典所有值为 : ", list(dic.values()))
# 字典所有值为 : [7, 'female', 'Zara']

dic = {'Name': 'Lsgogroup', 'Age': 7}
print("Value : %s" % dic.items())
# Value : dict_items([('Name', 'Lsgogroup'), ('Age', 7)])

"""
5. dict.get(key, default=None) 返回指定键的值，如果值不在字典中返回默认值
6. dict.setdefault(key, default=None) 和 get() 方法 类似, 如果键不存在于字典中，将会添加键并将值设为默认值。
7.  key in dict in 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true ，否则返回 false 。 
而 not in 操作符刚好相反，如果键在字典 dict 里返回 false ，否则返回 true 。
8. dict.pop(key[,default]) 删除字典给定键 key 所对应的值，返回值为被删除的值。 key 值必须给出。若 key
不存在，则返回 default 值。
9. del dict[key] 删除字典给定键 key 所对应的值。
10. dict.popitem() 随机返回并删除字典中的一对键和值，如果字典已经为空，却调用了此方法，就报出KeyError异常。
11.  dict.clear() 用于删除字典内所有元素。
"""
dic = {'Name': 'Lsgogroup', 'Age': 27}
print("Age 值为 : %s" % dic.get('Age')) # Age 值为 : 27

dic = {'Name': 'Lsgogroup', 'Age': 7}
print("Age 键的值为 : %s" % dic.setdefault('Age', None)) # Age 键的值为 : 7

dic = {'Name': 'Lsgogroup', 'Age': 7}
# in 检测键 Age 是否存在
if 'Age' in dic:
 print("键 Age 存在")
else:
 print("键 Age 不存在")
# 检测键 Sex 是否存在

dic1 = {1: "a", 2: [1, 2]}
print(dic1.pop(1), dic1) # a {2: [1, 2]}

dic = {'Name': 'Zara', 'Age': 7}
print("字典长度 : %d" % len(dic)) # 字典长度 : 2

"""
12. dict.copy() 返回一个字典的浅复制。
13. dict.update(dict2) 把字典参数 dict2 的 key:value 对 更新到字典 dict 里。
"""
dic1 = {'Name': 'Lsgogroup', 'Age': 7, 'Class': 'First'}
dic2 = dic1.copy()
print("新复制的字典为 : ", dic2)
# 新复制的字典为 : {'Age': 7, 'Name': 'Lsgogroup', 'Class': 'First'}