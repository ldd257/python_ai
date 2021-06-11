"""
元组相关的操作符 1. 比较操作符
2. 逻辑操作符
3. 连接操作符 + 4. 重复操作符 * 5. 成员关系操作符 in 、 not in
"""

# 元组拼接 (concatenate) 有两种方式，用「加号 +」和「乘号 *」，前者首尾拼接，后者复制拼接。
t1 = (2, 3, 4, 5)
t2 = ('老马的程序人生', '小马的程序人生')
t3 = t1 + t2
print(t3)
# (2, 3, 4, 5, '老马的程序人生', '小马的程序人生')
t4 = t2 * 2
print(t4)
# ('老马的程序人生', '小马的程序人生', '老马的程序人生', '小马的程序人生')

"""
内置方法
元组大小和内容都不可更改，因此只有 count 和 index 两种方法。

1. count('python') 是记录在元组 t 中该元素出现几次，显然是 1 次
2. index(10.31) 是找到该元素在元组 t 的索引，显然是 1
"""
t = (1, 10.31, 'python')
print(t.count('python')) # 1
print(t.index(10.31)) # 1


# 解压（unpack）一维元组（有几个元素左边括号定义几个变量）
t = (1, 10.31, 'python')
(a, b, c) = t
print(a, b, c)
# 1 10.31 python

"""
如果你只想要元组其中几个元素，用通配符「*」，英文叫 wildcard，在计算机语言中代表一个或多个元素。下例
就是把多个元素丢给了 rest 变量。
"""
t = 1, 2, 3, 4, 5
a, b, *rest, c = t
print(a, b, c) # 1 2 5
print(rest) # [3, 4]