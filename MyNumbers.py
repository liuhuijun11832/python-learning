class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

    def printtttt(self, str):
        print(str)
        return


myClass = MyNumbers()
myite = iter(myClass)
print(next(myite))
print(next(myite))
print(next(myite))
print(next(myite))


# 定义一个函数，并指定参数的默认值
def printme(str="hello"):
    print(str)
    return


printme()


# 参数带一个*号表示不定长参数，会以元组的形式导入
def printinfo( arg1, *vartuple):
    print("输出:")
    print(arg1)
    print(vartuple)


printinfo(70, 60, 50)


# 参数带两个*号表示使用字典形式导入不定长参数
def printinfo1( arg1, **vardict):
    print("输出:")
    print(arg1)
    print(vardict)


printinfo1(1, a=1, b=2)


# lambda函数的语法
sum = lambda arg1, arg2: arg1 + arg2
print("相加后的值为： ", sum(10, 20))


"""变量作用域： L-local：局部变量 E-enclosing: 闭包函数外的函数中 G-global:全局作用域 B-bulit-in：内置作用域 按照L-E-G-B的规则使用"""
"""内置作用域是通过一个名为builtin的标准模块来实现的，但是这个变量名并没有引入内置作用域内，所以需要首先导入才能使用它"""
# 通过这种方式可以看到预先定义了哪些变量
import builtins
print(dir(builtins))


"""python中只有模块-module，类-class以及函数-def才会引入新的作用域，其他的代码块比如if/else，try/except，for/while等是不会引入新的作用域的，也就是这些代码块内定的变量在外部是可以访问
的"""
if True:
    msg = "royal never give up"
print(msg)


# global和nonlocal关键字可以让内部作用域修改为外部作用域

num = 1


def fun1():
    # 函数会引入新的作用域，所以这里的num不加global无法引用外部的num
    global num
    print(num)
    num = 123
    print(num)


def fun2():
    num1 = 10

    def inner():
        # nonlocal关键字可以将enclosing作用域中的变量修饰为内部函数可以引用
        nonlocal num1
        num1 = 100
        print(num1)
    inner()
    print(num1)
fun2()