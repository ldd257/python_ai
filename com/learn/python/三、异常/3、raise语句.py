"""
使用 raise 语句抛出一个指定的异常。
"""
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')