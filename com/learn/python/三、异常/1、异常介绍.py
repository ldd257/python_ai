"""
Python 标准异常总结
1. BaseException：所有异常的 基类 2. Exception：常规异常的 基类 3. StandardError：所有的内建标准异常的基类
4. ArithmeticError：所有数值计算异常的基类
5. FloatingPointError：浮点计算异常
6. OverflowError：数值运算超出最大限制
7. ZeroDivisionError：除数为零
8. AssertionError：断言语句（assert）失败
9. AttributeError：尝试访问未知的对象属性
10. EOFError：没有内建输入，到达EOF标记
11. EnvironmentError：操作系统异常的基类
12. IOError：输入/输出操作失败
13. OSError：操作系统产生的异常（例如打开一个不存在的文件）
14. WindowsError：系统调用失败
15. ImportError：导入模块失败的时候
16. KeyboardInterrupt：用户中断执行
17. LookupError：无效数据查询的基类
18. IndexError：索引超出序列的范围
19. KeyError：字典中查找一个不存在的关键字
20. MemoryError：内存溢出（可通过删除对象释放内存）
21. NameError：尝试访问一个不存在的变量
22. UnboundLocalError：访问未初始化的本地变量
23. ReferenceError：弱引用试图访问已经垃圾回收了的对象
24. RuntimeError：一般的运行时异常
25. NotImplementedError：尚未实现的方法
26. SyntaxError：语法错误导致的异常
27. IndentationError：缩进错误导致的异常
28. TabError：Tab和空格混用
29. SystemError：一般的解释器系统异常
30. TypeError：不同类型间的无效操作
31. ValueError：传入无效的参数
32. UnicodeError：Unicode相关的异常
33. UnicodeDecodeError：Unicode解码时的异常
34. UnicodeEncodeError：Unicode编码错误导致的异常
35. UnicodeTranslateError：Unicode转换错误导致的异常
"""

"""
Python标准警告总结
1. Warning：警告的基类
2. DeprecationWarning：关于被弃用的特征的警告
3. FutureWarning：关于构造将来语义会有改变的警告
4. UserWarning：用户代码生成的警告
5. PendingDeprecationWarning：关于特性将会被废弃的警告
6. RuntimeWarning：可疑的运行时行为(runtime behavior)的警告
7. SyntaxWarning：可疑语法的警告
8. ImportWarning：用于在导入模块过程中触发的警告
9. UnicodeWarning：与Unicode相关的警告
10. BytesWarning：与字节或字节码相关的警告
11. ResourceWarning：与资源使用相关的警告
"""