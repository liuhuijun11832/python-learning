# -*- coding: utf-8 -*-
import keyword
import sys

print("hello world")
print("hello ", end="")
print("world")
print(keyword.kwlist)

# !/usr/bin/python3

# 第一个注释
# 第二个注释

'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""
# 基本类型
a = b = c = 1
a, b, c = 1, 2, "hello world"
# 不可变：Number，String，Tuple
# 可变：List，Dictionary，Set

# Number：int,float,boolean,complex
a = 20
b = 5.5
c = True
d = 4+3j
print(isinstance(a, int))
print(type(a) == int)


class A:
    pass


class B(A):
    pass


print(isinstance(A(), A))
print(type(A()) == A)
print(isinstance(B(), A))
print(type(B()) == A)
# ininstance和type的区别在于type不认为子类是一种父类类型
# python3中虽然有boolean类型，但是True实际上是1，False实际上是0，它们都可以和数字相加

del a

print(5+4)
print(5**2)
print(5/2)
print(5//2)

# string，python中字符串就是字符，使用单引号或者双引号括起来，截取方法：变量[头下标：尾下标]，下标可以是负数，+代表字符串连接，*代表字符串复制
print("1"*3)
# 使用r可以避免\转义
print(r"liuhuijun\r")
# 字符串格式化
print("我叫 %s ,今年 %d 岁！" % ('小明', 10))
# 使用连续的三个引号可以使用跨越多行的字符串
# python中字符串元素不能够改变
st = "hello World"
# st[0, 2] = []
print(len(st))
print(type(st))
print(st.count("he"))


# list 用的最多的数据类型
listInt = [1, 2, 3, 4, 5, 6]
print(listInt)
print(listInt[1:4:2])
listInt[0:1] = []
print(listInt)
# list可以改变其中某个元素
listInt[1] = 33
print(listInt)


# tuple元组,可以包含不同类型的数据类型
listIns = ['abcd', 33, 2.23, "hello world"]
# list使用方括号，元组使用括号，,只有一个元素的时候需要加逗号，不然括号会当作运算符使用
tup1 = (50,)
for x in listIns:
    print(x, end=" ")
print(listIns)
print(listIns[0:3])
print(listIns[0:3] * 2)

# set集合 无序不重复，使用{}（空字典）或者set()函数创建集合
student = {'Tom', 'Jack', 'Joy', 'Tom', 'Thomas'}
print(student)

if 'Tom' in student:
    print("Tom is in student")
else:
    print("Tom is not in student")

# set进行集合运算
a = set("abababcdddeee")
b = set("ababfgqpe")

print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

# Dictionary 字典，通过键来取存取，使用{}来创建，它是一个无序的键(key):值(value)的集合
# 键必须是不可变元素
dic = {}
dic['one'] = "这是第一个元素"
dic[2] = "这是第二个元素"
print(dic.keys())
print(dic.values())

tinyDict = {'name': 'google', 'code': 1, 'site': 'www.guitar-docer.cn'}
print(tinyDict.keys())
print(tinyDict.values())
print("Tinydict['name']", tinyDict['name'])
# 字典里的元素允许被修改和删除
tinyDict['name'] = 'alibaba'
print("Tinydict['name']", tinyDict['name'])
print("name" in tinyDict)


shopDict = dict([('taobao', 1), ('tianmao', 2), ('jingdong', 3)])
print(shopDict)
a = 20
b = 20

# is和==的区别：is用于判断两个变量引用是否为同一个，==用于判断引用变量的值是否相等
if a is b:
    print("a 和 b 具有相同的标识")
else:
    print("a 和 b 具有不同的标识")

if id(a) == id(b):
    print("a 和 b 具有相同的标识")
else:
    print("a 和 b 具有不同的标识")

b = 30
if a is b:
    print("a 和 b 具有相同的标识")
else:
    print("a 和 b 具有不同的标识")

if id(a) == id(b):
    print("a 和 b 具有相同的标识")
else:
    print("a 和 b 具有不同的标识")

# 运算符 //可以表示只取整数部分，但是与分子分母的格式有关系
print(7/2)
print(7//2)
print(7.0//2)
print(7//2.0)

# 计算1到100的之和
n = 100
count = 1
sum = 0
while count <= n:
    sum += count
    count += 1
print("从1 到 %d 的数之和为 %d" % (n, sum))
# range函数可以用来生成一个数字序列，或者指定区间内的数字序列
for i in range(5):
    print(i)
print(list(range(5)))

# 循环中可以使用else语句，break会导致循环的else不被执行，continue会跳过当前循环的剩余语句，开始执行循环的下一个元素
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 内层循环中没有找到元素
        print(n, "是质数")

# python迭代器和生成器
it = iter(tinyDict)
# 第一种循环方式
for x in it:
    print(x, tinyDict[x])
# 第二种循环方式
it = iter(tinyDict)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()

MyNumbers.printtttt("jjjjjj")
# 可以对函数进行赋值引用
fun = MyNumbers.printtttt
fun("adjfladf")


