# 1. 创建一个普通列表
x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(x, type(x))

# 2. 利用 range() 创建列表
x2 = list(range(1, 3))

# 3. 利用推导式创建列表
x3 = [0] ** 3
x4 = [v for v in range(1, 3)]


"""
由于list的元素可以是任何对象，因此列表中所保存的是对象的指针。即使保存一个简单的 [1,2,3] ，也有3个指针和3个
整数对象
"""
# 4. 二维数组
xx = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 0, 0]]
print(x, type(x))

# 5. 创建一个混合列表
mix = [1, 'lsgo', 3.14, [1, 2, 3]]

# 6. 创建一个空列表
empty = []