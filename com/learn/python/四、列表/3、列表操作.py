"""
列表不像元组，列表内容可更改 (mutable)，因此附加 ( append , extend )、插入 ( insert )、删除 ( remove , pop ) 这些
操作都可以用在它身上。
"""
# 1. 追加元素
"""
list.append(obj) 在列表末尾添加新的对象，只接受一个参数，参数可以是任何数据类型，被追加的元素在 list
中保持着原结构类型。
 list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
 严格来说 append 是追加，把一个东西整体添加在列表后，而 extend 是扩展，把一个东西里的所有元素添加在列表
后。
"""
className = ["张三"]
className.append("李四")

className.extend(["王五", "赵六"])


# 2. list.insert(index, obj) 在编号 index 位置前插入 obj 。
className.insert(1, "小美")

"""
3. list.remove(obj) 移除列表中某个值的第一个匹配项
list.pop([index=-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

remove 和 pop 都可以删除元素，前者是指定具体要删除的元素，后者是指定一个索引
"""
className.remove("赵六")
className.pop()

"""
4.  del var1[, var2 ……] 删除单个或多个对象
如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用 del 语句；如果你要在删除元素后还能继续使用它，
就使用方法 pop()
"""

del className


"""
5. 查询
1. 通过元素的索引值，从列表获取单个元素，注意，列表索引值是从0开始的。
2. 通过将索引指定为-1，可让Python返回最后一个列表元素，索引 -2 返回倒数第二个列表元素，以此类推

切片的通用写法是 start : stop : step
1. 情况 1 - "start :"
2. 以 step 为 1 (默认) 从编号 start 往列表尾部切片。
"""
x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(x[3:]) # ['Thursday', 'Friday']
print(x[-3:]) # ['Wednesday', 'Thursday', 'Friday']

"""
1. 情况 2 - ": stop"
2. 以 step 为 1 (默认) 从列表头部往编号 stop 切片。
"""
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(week[:3]) # ['Monday', 'Tuesday', 'Wednesday']
print(week[:-3]) # ['Monday', 'Tuesday']

"""
1. 情况 3 - "start : stop"
2. 以 step 为 1 (默认) 从编号 start 往编号 stop 切片。
"""
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(week[1:3]) # ['Tuesday', 'Wednesday']
print(week[-3:-1]) # ['Wednesday', 'Thursday']


"""
1. 情况 4 - "start : stop : step"
2. 以具体的 step 从编号 start 往编号 stop 切片。注意最后把 step 设为 -1，相当于将列表反向排列。
"""
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(week[1:4:2])
# ['Tuesday', 'Thursday']

"""
1. 情况 5 - " : "
2. 复制列表中的所有元素（浅拷贝）。
"""
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(week[:])


"""
列表的常用操作符 
1. 等号操作符： ==
2. 连接操作符 + 
3. 重复操作符 * 
4. 成员关系操作符 in 、 not in
「等号 ==」，只有成员、成员位置都相同时才返回True。
和元组拼接一样， 列表拼接也有两种方式，用「加号 +」和「乘号 *」，前者首尾拼接，后者复制拼接。
"""


"""
列表的其它方法
list.count(obj) 统计某个元素在列表中出现的次数
list.index(x[, start[, end]]) 从列表中找出某个值第一个匹配项的索引位置
list.reverse() 反向列表中元素

list.sort(key=None, reverse=False) 对原列表进行排序。
1. key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象
中的一个元素来进行排序。
2. reverse -- 排序规则， reverse = True 降序， reverse = False 升序（默认）。
3. 该方法没有返回值，但是会对列表的对象进行排序
"""
list1 = [123, 456] * 3
print(list1) # [123, 456, 123, 456, 123, 456]
num = list1.count(123)
print(num) # 3

list1 = [123, 456] * 5
print(list1.index(123)) # 0

x = [123, 456, 789]
x.reverse()
print(x) # [789, 456, 123]
