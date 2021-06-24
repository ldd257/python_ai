"""
Python 的 self 相当于 C++ 的 this 指针。
类的方法与普通的函数只有一个特别的区别 —— 它们必须有一个额外的第一个参数名称（对应于该实例，即该对象本
身），按照惯例它的名称是 self 。在调用方法时，我们无需明确提供与参数 self 相对应的参数。
"""
class Test:
    def prt(self):
        print(self)
        print(self.__class__)
t = Test()
t.prt()
# <__main__.Test object at 0x000000BC5A351208>
# <class '__main__.Test'>


class Ball:
    def setName(self, name):
        self.name = name
    def kick(self):
        print("我叫%s,该死的，谁踢我..." % self.name)
a = Ball()
a.setName("球A")
b = Ball()
b.setName("球B")
c = Ball()
c.setName("球C")
a.kick()
# 我叫球A,该死的，谁踢我...
b.kick()
# 我叫球B,该死的，谁踢我...


"""
Python的魔法方法
据说，Python 的对象天生拥有一些神奇的方法，它们是面向对象的 Python 的一切...
它们是可以给你的类增加魔力的特殊方法...
如果你的对象实现了这些方法中的某一个，那么这个方法就会在特殊的情况下被 Python 所调用，而这一切都是自动发生
的...
类有一个名为 __init__(self[, param1, param2...]) 的魔法方法，该方法在类实例化时会自动调用。
"""
class Ball:
    def __init__(self, name):
        self.name = name
    def kick(self):
        print("我叫%s,该死的，谁踢我..." % self.name)
a = Ball("球A")
b = Ball("球B")
c = Ball("球C")
a.kick()
# 我叫球A,该死的，谁踢我...
b.kick()
# 我叫球B,该死的，谁踢我...

"""
公有和私有 
在 Python 中定义私有变量只需要在变量名或函数名前加上“__”两个下划线，那么这个函数或变量就会为私有的了。
"""
class JustCounter:
    __secretCount = 0 # 私有变量
    publicCount = 0 # 公开变量
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)
counter = JustCounter()
counter.count() # 1
counter.count() # 2
print(counter.publicCount) # 2
print(counter._JustCounter__secretCount) # 2 Python的私有为伪私有
print(counter.__secretCount)
# AttributeError: 'JustCounter' object has no attribute '__secretCount'


# 类的私有方法实例
class Site:
    def __init__(self, name, url):
        self.name = name # public
        self.__url = url # private

        def who(self):
            print('name : ', self.name)
            print('url : ', self.__url)

            def __foo(self):  # 私有方法
                print('这是私有方法')

            def foo(self):  # 公共方法
                print('这是公共方法')

            self.__foo()

x = Site('老马的程序人生', 'https://blog.csdn.net/LSGO_MYP')
x.who()
# name : 老马的程序人生
# url : https://blog.csdn.net/LSGO_MYP
x.foo()
# 这是公共方法
# 这是私有方法
x.__foo()
# AttributeError: 'Site' object has no attribute '__foo'