# -*- coding: utf-8 -*-

while True:
    try:
        x = int(input("请输入一个数字："))
        break
    except ValueError:
        print("输入的不是数字。")
"""执行try语句，如果没有发生异常就忽略except语句，发生异常就执行excep语句；如果没有excep与之对应，会传递给上层的try语句中。except后可以跟多个错误excep ()"""
"""最后一个excep子句可以忽略异常的名称，它将被当作通配符使用"""

try:
    f = open("E:\\data.pkl")
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:{0}".format(err))
except ValueError:
    print("could not convert data to an integer.")
# 一般情况下，不推荐这种裸露的excep
# except:
#     print("unexcepted error :", sys.exc_info()[0])
#     raise
# 使用else要放在所有excep之后，表示没有发生异常的时候执行else里的语句，这样可以避免一些意想不到的，而excep又没有捕获的异常
else:
    print("哈哈哈，没有任何异常")


# try可以捕捉子句和间接调用的子函数里的异常，raise可以将异常直接抛出
# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise


'''用户自定义异常'''


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)
# 不管try子句里有没有异常，finally子句都会执行，如果一个异常在try子句中抛出，而又没有任何有的excep把它截住，那么这个异常会在finally子句执行后被抛出
finally:
    print("无论有没有异常，这句一定会执行")

'''当创建一个模块有可能抛出多种不同的异常时，通常会为这个包建立一个基础异常类，然后基于这个基础类为不同的错误情况创建不同的子类'''


class Error(Exception):
    # 用户模块自定义异常基类
    pass


class InputError(Error):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class TransitionError(Error):
    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message


'''预定义的清理行为'''
# 这行代码执行完，但是没有释放文件
for line in open("E:\\test.txt", "r"):
    print(line, end="")
# 这行代码执行完毕无论处理过程中有没有问题，文件总会被关闭
with open("E:\\data.pkl") as f:
    for line in f:
        print(line, end="")