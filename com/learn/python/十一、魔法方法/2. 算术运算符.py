"""
算术运算符
类型工厂函数，指的是不通过类而是通过函数来创建对象。
"""

class C:
 pass
print(type(len)) # <class 'builtin_function_or_method'>
print(type(dir)) # <class 'builtin_function_or_method'>
print(type(int)) # <class 'type'>
print(type(list)) # <class 'type'>
print(type(tuple)) # <class 'type'>
print(type(C)) # <class 'type'>
print(int('123')) # 123
# 这个例子中list工厂函数把一个元祖对象加工成了一个列表对象。
print(list((1, 2, 3))) # [1, 2, 3]

"""
1. __add__(self, other) 定义加法的行为： +
2. __sub__(self, other) 定义减法的行为： -

1. __mul__(self, other) 定义乘法的行为： *
2. __truediv__(self, other) 定义真除法的行为： /
3. __floordiv__(self, other) 定义整数除法的行为： //
4. __mod__(self, other) 定义取模算法的行为： %
5. __divmod__(self, other) 定义当被 divmod() 调用时的行为
6. divmod(a, b) 把除数和余数运算结果结合起来，返回一个包含商和余数的元组 (a // b, a % b) 。

1. __pow__(self, other[, module]) 定义当被 power() 调用或 ** 运算时的行为
2. __lshift__(self, other) 定义按位左移位的行为： <<
3. __rshift__(self, other) 定义按位右移位的行为： >>
4. __and__(self, other) 定义按位与操作的行为： &
5. __xor__(self, other) 定义按位异或操作的行为： ^
6. __or__(self, other) 定义按位或操作的行为： |
"""



"""
反算术运算符
反运算魔方方法，与算术运算符保持一一对应，不同之处就是反运算的魔法方法多了一个“r”。当文件左操作不支持相应的
操作时被调用。
1. __radd__(self, other) 定义加法的行为： +
2. __rsub__(self, other) 定义减法的行为： -
3. __rmul__(self, other) 定义乘法的行为： *
4. __rtruediv__(self, other) 定义真除法的行为： /
5. __rfloordiv__(self, other) 定义整数除法的行为： //
6. __rmod__(self, other) 定义取模算法的行为： %
7. __rdivmod__(self, other) 定义当被 divmod() 调用时的行为
8. __rpow__(self, other[, module]) 定义当被 power() 调用或 ** 运算时的行为
9. __rlshift__(self, other) 定义按位左移位的行为： <<
10. __rrshift__(self, other) 定义按位右移位的行为： >>
11. __rand__(self, other) 定义按位与操作的行为： &
12. __rxor__(self, other) 定义按位异或操作的行为： ^
13. __ror__(self, other) 定义按位或操作的行为： |


a + b
这里加数是 a ，被加数是 b ，因此是 a 主动，反运算就是如果 a 对象的 __add__() 方法没有实现或者不支持相应的操
作，那么 Python 就会调用 b 的 __radd__() 方法。
"""
class Nint(int):
 def __radd__(self, other):
    return int.__sub__(other, self) # 注意 self 在后面
a = Nint(5)
b = Nint(3)
print(a + b) # 8
print(1 + b) # -2

""""
增量赋值运算符
1. __iadd__(self, other) 定义赋值加法的行为： +=
2. __isub__(self, other) 定义赋值减法的行为： -=
3. __imul__(self, other) 定义赋值乘法的行为： *=
4. __itruediv__(self, other) 定义赋值真除法的行为： /=
5. __ifloordiv__(self, other) 定义赋值整数除法的行为： //=
6. __imod__(self, other) 定义赋值取模算法的行为： %=
7. __ipow__(self, other[, modulo]) 定义赋值幂运算的行为： **=
8. __ilshift__(self, other) 定义赋值按位左移位的行为： <<=
9. __irshift__(self, other) 定义赋值按位右移位的行为： >>=
10. __iand__(self, other) 定义赋值按位与操作的行为： &=
11. __ixor__(self, other) 定义赋值按位异或操作的行为： ^=
12. __ior__(self, other) 定义赋值按位或操作的行为： |=
"""

"""

一元运算符
1. __neg__(self) 定义正号的行为： +x
2. __pos__(self) 定义负号的行为： -x
3. __abs__(self) 定义当被 abs() 调用时的行为
4. __invert__(self) 定义按位求反的行为： ~x


属性访问
__getattr__ ， __getattribute__ ， __setattr__ 和 __delattr__
__getattr__(self, name) : 定义当用户试图获取一个不存在的属性时的行为。
__getattribute__(self, name) ：定义当该类的属性被访问时的行为（先调用该方法，查看是否存在该属性，若不存
在，接着去调用 __getattr__ ）。
__setattr__(self, name, value) ：定义当一个属性被设置时的行为。
__delattr__(self, name) ：定义当一个属性被删除时的行为。



描述符
描述符就是将某种特殊类型的类的实例指派给另一个类的属性。
1. __get__(self, instance, owner) 用于访问属性，它返回属性的值。
2. __set__(self, instance, value) 将在属性分配操作中调用，不返回任何内容。
3. __del__(self, instance) 控制删除操作，不返回任何内容。


定制序列
协议（Protocols）与其它编程语言中的接口很相似，它规定你哪些方法必须要定义。然而，在 Python 中的协议就显得不那
么正式。事实上，在 Python 中，协议更像是一种指南。
容器类型的协议
1. 如果说你希望定制的容器是不可变的话，你只需要定义 __len__() 和 __getitem__() 方法。
2. 如果你希望定制的容器是可变的话，除了 __len__() 和 __getitem__() 方法，你还需要定义 __setitem__()
和 __delitem__() 两个方法。

迭代器
1. 迭代是 Python 最强大的功能之一，是访问集合元素的一种方式。
2. 迭代器是一个可以记住遍历的位置的对象。
3. 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
4. 迭代器只能往前不会后退。
5. 字符串，列表或元组对象都可用于创建迭代器：

1. 迭代器有两个基本的方法： iter() 和 next() 。
2. iter(object) 函数用来生成迭代器。
3. next(iterator[, default]) 返回迭代器的下一个项目。
4. iterator -- 可迭代对象
5. default -- 可选，用于设置在没有下一个元素时返回该默认值，如果不设置，又没有下一个元素则会触发
StopIteration 异常。

把一个类作为一个迭代器使用需要在类中实现两个魔法方法 __iter__() 与 __next__() 。
1. __iter__(self) 定义当迭代容器中的元素的行为，返回一个特殊的迭代器对象， 这个迭代器对象实现了
__next__() 方法并通过 StopIteration 异常标识迭代的完成。
2. __next__() 返回下一个迭代器对象。
3. StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完
成指定循环次数后触发 StopIteration 异常来结束迭代


生成器
1. 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
2. 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
3. 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下
一次执行 next() 方法时从当前位置继续运行。
4. 调用一个生成器函数，返回的是一个迭代器对象。
"""