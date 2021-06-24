"""
对象 = 属性 + 方法
对象是类的实例。换句话说，类主要定义对象的结构，然后我们以类为模板创建对象。类不但包含方法定义，而且还包含
所有实例共享的数据。
1. 封装：信息隐蔽技术
我们可以使用关键字 class 定义 Python 类，关键字后面紧跟类的名称、分号和类的实现。
"""
class Turtle: # Python中的类名约定以大写字母开头
    """关于类的一个简单例子"""
    # 属性
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouth = '大嘴'
    # 方法
    def climb(self):
        print('我正在很努力的向前爬...')
    def run(self):
        print('我正在飞快的向前跑...')
    def bite(self):
        print('咬死你咬死你!!')
    def eat(self):
        print('有得吃，真满足...')
    def sleep(self):
        print('困了，睡了，晚安，zzz')


tt = Turtle()
print(tt.weight)
print(tt)
# <__main__.Turtle object at 0x0000007C32D67F98>
print(type(tt))
# <class '__main__.Turtle'>
print(tt.__class__)
# <class '__main__.Turtle'>
print(tt.__class__.__name__)
# Turtle
tt.climb()
# 我正在很努力的向前爬...
tt.run()
# 我正在飞快的向前跑...
tt.bite()
# 咬死你咬死你!!
# Python类也是对象。它们是type的实例
print(type(Turtle))
# <class 'type'>


# 继承：子类自动共享父类之间数据和方法的机制

class MyList(list):
 pass
lst = MyList([1, 5, 2, 7, 8])
lst.append(9)
lst.sort()
print(lst)
# [1, 2, 5, 7, 8, 9]

"""
Python 同样支持类的继承，派生类的定义如下所示：
class DerivedClassName(BaseClassName):
 <statement-1>
 .
 .
 .
 <statement-N>
 
 BaseClassName （示例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个
模块中时这一点非常有用：
class DerivedClassName(modname.BaseClassName):
 <statement-1>
 .
 .
 .
 <statement-N>
 如果子类中定义与父类同名的方法或属性，则会自动覆盖父类对应的方法或属性。
"""
# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))
# 单继承示例
class student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g
    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))
s = student('小马的程序人生', 10, 60, 3)
s.speak()
# 小马的程序人生 说: 我 10 岁了，我在读 3 年级
"""
注意：如果上面的程序去掉： people.__init__(self, n, a, w) ，则输出： 说: 我 0 岁了，我在读 3 年级 ，因为
子类的构造方法把父类的构造方法覆盖了
解决：people.__init__(self, n, a, w) 
1. 调用未绑定的父类方法 Fish.__init__(self)
2. 使用super函数 super().__init__()
"""

"""
多继承问题
Python 虽然支持多继承的形式，但我们一般不使用多继承，因为容易引起混乱。
class DerivedClassName(Base1, Base2, Base3):
 <statement-1>
 .
 .
 .
 <statement-N>
 需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，Python 从左至右搜索，即方法在子
类中未找到时，从左到右查找父类中是否包含方法。
"""




# 多态：不同对象对同一方法响应不同的行动
class Animal:
    def run(self):
        raise AttributeError('子类必须实现这个方法')
class People(Animal):
    def run(self):
        print('人正在走')
class Pig(Animal):
    def run(self):
        print('pig is walking')
class Dog(Animal):
    def run(self):
        print('dog is running')
def func(animal):
    animal.run()

func(Pig())
# pig is walking