"""
集合的内置方法
1. set.add(elmnt) 用于给集合添加元素，如果添加的元素在集合中已存在，则不执行任何操作。
2. set.update(set) 用于修改当前集合，可以添加新的元素或集合到当前集合中，如果添加的元素在集合中已存在，
则该元素只会出现一次，重复的会忽略
4. set.remove(item) 用于移除集合中的指定元素。如果元素不存在，则会发生错误。
5. set.discard(value) 用于移除指定的集合元素。 remove() 方法在移除一个不存在的元素时会发生错误，而discard() 方法不会。
"""
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
# {'orange', 'cherry', 'banana', 'apple'}

x = {"apple", "banana", "cherry"}
y = {"google", "baidu", "apple"}
x.update(y)
print(x)
# {'cherry', 'banana', 'apple', 'google', 'baidu'}

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits) # {'apple', 'cherry'}

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits) # {'apple', 'cherry'}


"""
6. set.pop() 用于随机移除一个元素
7. 由于 set 是无序和无重复元素的集合，所以两个或多个 set 可以做数学意义上的集合操作。
    1. set.intersection(set1, set2 ...) 返回两个集合的交集。
    2. set1 & set2 返回两个集合的交集。
    3. set.intersection_update(set1, set2 ...) 交集，在原始的集合上移除不重叠的元素

8. set.union(set1, set2...) 返回两个集合的并集。
    1. set1 | set2 返回两个集合的并集。
    
9.  1. set.difference(set) 返回集合的差集。
    2. set1 - set2 返回集合的差集。
    3. set.difference_update(set) 集合的差集，直接在原来的集合中移除元素，没有返回值。

10. 1. set.symmetric_difference(set) 返回集合的异或。
    2. set1 ^ set2 返回集合的异或。
    3. set.symmetric_difference_update(set) 移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
"""
a = set('abracadabra')
b = set('alacazam')
print(a) # {'r', 'a', 'c', 'b', 'd'}
print(b) # {'c', 'a', 'l', 'm', 'z'}
c = a.intersection(b)
print(c) # {'a', 'c'}
print(a & b) # {'c', 'a'}
print(a) # {'a', 'r', 'c', 'b', 'd'}
a.intersection_update(b)
print(a) # {'a', 'c'}

a = set('abracadabra')
b = set('alacazam')
print(a) # {'r', 'a', 'c', 'b', 'd'}
print(b) # {'c', 'a', 'l', 'm', 'z'}
print(a | b) # {'l', 'd', 'm', 'b', 'a', 'r', 'z', 'c'}
c = a.union(b)
print(c) # {'c', 'a', 'd', 'm', 'r', 'b', 'z', 'l'}

a = set('abracadabra')
b = set('alacazam')
print(a) # {'r', 'a', 'c', 'b', 'd'}
print(b) # {'c', 'a', 'l', 'm', 'z'}
c = a.difference(b)
print(c) # {'b', 'd', 'r'}
print(a - b) # {'d', 'b', 'r'}

a = set('abracadabra')
b = set('alacazam')
print(a) # {'r', 'a', 'c', 'b', 'd'}
print(b) # {'c', 'a', 'l', 'm', 'z'}
c = a.symmetric_difference(b)
print(c) # {'m', 'r', 'l', 'b', 'z', 'd'}
print(a ^ b) # {'m', 'r', 'l', 'b', 'z', 'd'}

"""
11. set.issubset(set) 判断集合是不是被其他集合包含，如果是则返回 True，否则返回 False。
    1. set1 <= set2 判断集合是不是被其他集合包含，如果是则返回 True，否则返回 False。
12. set.issuperset(set) 用于判断集合是不是包含其他集合，如果是则返回 True，否则返回 False。
    1. set1 >= set2 判断集合是不是包含其他集合，如果是则返回 True，否则返回 False。
13. set.isdisjoint(set) 用于判断两个集合是不是不相交，如果是返回 True，否则返回 False。
"""
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z) # True
print(x <= y) # True
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
z = x.issubset(y)
print(z) # False
print(x <= y) # False

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z) # True
print(x >= y) # True
x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z) # False
print(x >= y) # False

x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.isdisjoint(y)
print(z) # False
x = {"f", "e", "d", "m", "g"}
y = {"a", "b", "c"}
z = x.isdisjoint(y)
print(z) # True


# 集合的转换
se = set(range(4))
li = list(se)
tu = tuple(se)
print(se, type(se)) # {0, 1, 2, 3} <class 'set'>
print(li, type(li)) # [0, 1, 2, 3] <class 'list'>
print(tu, type(tu)) # (0, 1, 2, 3) <class 'tuple'>

"""
不可变集合
Python 提供了不能改变元素的集合的实现版本，即不能增加或删除元素，类型名叫 frozenset 。需要注意的
是 frozenset 仍然可以进行集合操作，只是不能用带有 update 的方法。
1. frozenset([iterable]) 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
"""
a = frozenset(range(10)) # 生成一个新的不可变集合
print(a)
# frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
b = frozenset('lsgogroup')
print(b)
# frozenset({'g', 's', 'p', 'r', 'u', 'o', 'l'})