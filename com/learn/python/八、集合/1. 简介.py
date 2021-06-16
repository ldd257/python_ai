"""
集合
python 中 set 与 dict 类似，也是一组 key 的集合，但不存储 value 。由于 key 不能重复，所以，在 set 中，没有重复的 key 。
注意， key 为不可变类型，即可哈希的值。

从结果发现集合的两个特点：无序 (unordered) 和唯一 (unique)。
由于 set 存储的是无序集合，所以我们不可以为集合创建索引或执行切片(slice)操作，也没有键(keys)可用来获取集合中
元素的值，但是可以判断一个元素是否在集合中。
"""
num = {}
print(type(num)) # <class 'dict'>
num = {1, 2, 3, 4}
print(type(num)) # <class 'set'>


"""
集合的创建
1. 先创建对象再加入元素。
2. 在创建空集合的时候只能使用 s = set() ，因为 s = {} 创建的是空字典。
3. 直接把一堆元素用花括号括起来 {元素1, 元素2, ..., 元素n} 。
4. 重复元素在 set 中会被自动被过滤。
5. 使用 set(value) 工厂函数，把列表或元组转换成集合
"""
basket = set()
basket.add('apple')
basket.add('banana')
print(basket) # {'banana', 'apple'}

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # {'banana', 'apple', 'pear', 'orange'}

a = set('abracadabra')
print(a)
# {'r', 'b', 'd', 'c', 'a'}
b = set(("Google", "Lsgogroup", "Taobao", "Taobao"))
print(b)
# {'Taobao', 'Lsgogroup', 'Google'}
c = set(["Google", "Lsgogroup", "Taobao", "Google"])
print(c)
# {'Taobao', 'Lsgogroup', 'Google'}
