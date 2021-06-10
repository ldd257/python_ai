"""
break 语句可以跳出当前所在层的循环。跳出循环
continue 终止本轮循环并开始下一轮循环。跳过本次循环
"""
for i in range(1, 4):
    print("start=======", i)
    if i % 2 == 0:
        print("我是偶数，我可以跳过本次循环", i)
        continue

    if i == 3:
        print("当是3，我结束循环", i)
        break
    print("end=======", i)

"""
pass 语句的意思是“不做任何事”，如果你在需要有语句的地方不写任何语句，那么解释器会提示出错，而 pass 语句就
是用来解决这些问题的。
pass 是空语句，不做任何操作，只起到占位的作用，其作用是为了保持程序结构的完整性。尽管 pass 语句不做任何操
作，但如果暂时不确定要在一个位置放上什么样的代码，可以先放置一个 pass 语句，让代码可以正常运行。
"""
if True:
    pass


"""
推导式

"""
# 列表推导式
ex = [print(va) for va in range(1, 6)]

ex2 = [print(va) for va in range(1, 6) if va % 2 == 0]

# 元组
ex3 = (va for va in range(1, 6))

# 字典
ex4 = {va: va % 2 == 0 for va in range(1, 6)}

# 集合
ex5 = {va for va in range(1, 6)}
