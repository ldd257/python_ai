"""
try:
    检测范围
except Exception[as reason]:
    出现异常后的处理代码

try 语句按照如下方式工作：
1. 首先，执行 try 子句（在关键字 try 和关键字 except 之间的语句）
2. 如果没有异常发生，忽略 except 子句， try 子句执行后结束。
3. 如果在执行 try 子句的过程中发生了异常，那么 try 子句余下的部分将被忽略。如果异常的类型和 except 之后的
名称相符，那么对应的 except 子句将被执行。最后执行 try 语句之后的代码。
4. 如果一个异常没有与任何的 except 匹配，那么这个异常将会传递给上层的 try 中。

一个 try 语句可能包含多个 except 子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
"""
try:
    # 检测异常代码
    2/0
except Exception as ex:
    print(ex)


"""
try:
    检测范围
except:
    出现异常后的处理代码
else:
    如果没有异常执行这块代码

try-except-else 语句尝试查询不在 dict 中的键值对，从而引发了异常。这一异常准确地说应属于 KeyError ，但由
于 KeyError 是 LookupError 的子类，且将 LookupError 置于 KeyError 之前，因此程序优先执行该 except 代码块。
所以，使用多个 except 代码块时，必须坚持对其规范排序，要从最具针对性的异常到最通用的异常。

注意： else 语句的存在必须以 except 语句的存在为前提，在没有 except 语句的 try 语句中使用 else 语句，会引发
语法错误。
"""
try:
    # 检测异常代码
    2/1
except Exception as ex:
    print(ex)
else:
    print("无异常执行，检测结束")


"""
try:
    检测范围
except Exception[as reason]:
    出现异常后的处理代码
finally:
    无论如何都会被执行的代码

不管 try 子句里面有没有发生异常， finally 子句都会执行。
如果一个异常在 try 子句里被抛出，而又没有任何的 except 把它截住，那么这个异常会在 finally 子句执行后被抛出。
"""
try:
    # 检测异常代码
    2/1
except Exception as ex:
    print(ex)
finally:
    print("始终执行")


try:
    # 检测异常代码
    2/0
except Exception as ex:
    print(ex)
else:
    print("无异常执行，检测结束")
finally:
    print("始终执行")