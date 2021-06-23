"""
1. Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
2. 定义在函数内部的变量拥有局部作用域，该变量称为局部变量。
3. 定义在函数外部的变量拥有全局作用域，该变量称为全局变量。
4. 局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。
"""
def discounts(price, rate):
    final_price = price * rate
    return final_price
old_price = float(input('请输入原价:')) # 98
rate = float(input('请输入折扣率:')) # 0.9
new_price = discounts(old_price, rate)
print('打折后价格是:%.2f' % new_price) # 88.20


# 当内部作用域想修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字了。
num = 1
def fun1():
    global num # 需要使用 global 关键字声明
    print(num) # 1
    num = 123
    print(num) # 123
fun1()
print(num) # 123

# 内嵌函数
def outer():
    print('outer函数在这被调用')
    def inner():
        print('inner函数在这被调用')
    inner() # 该函数只能在outer函数内部被调用
outer()
# outer函数在这被调用
# inner函数在这被调用


"""
闭包
1. 是函数式编程的一个重要的语法结构，是一种特殊的内嵌函数。
2. 如果在一个内部函数里对外层非全局作用域的变量进行引用，那么内部函数就被认为是闭包。
3. 通过闭包可以访问外层非全局作用域的变量，这个作用域称为 闭包作用域。
"""
def funX(x):
    def funY(y):
        return x * y
    return funY
i = funX(8)
print(type(i)) # <class 'function'>
print(i(5)) # 40


# 如果要修改闭包作用域中的变量则需要 nonlocal 关键字
def outer():
    num = 10
    def inner():
        nonlocal num # nonlocal关键字声明
        num = 100
        print(num)
        inner()
        print(num)


outer()
# 100
# 100