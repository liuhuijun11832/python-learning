# -*- coding: utf-8 -*-
import keyword
print("hello world")
print("hello ",end="")
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
# 使用连续的三个引号可以使用跨越多行的字符串
# python中字符串元素不能够改变
st = "hello World"
# st[0, 2] = []
print(st)

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
print(listIns)
print(listIns[0:3])
print(listIns[0:3] * 2)

# set集合 无序不重复，使用{}（空字典）或者set{}函数创建集合
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
dic = {}
dic['one'] = "这是第一个元素"
dic[2] = "这是第二个元素"
print(dic.keys())
print(dic.values())

tinyDict = {'name': 'google', 'code': 1, 'site': 'www.guitar-docer.cn'}
print(tinyDict.keys())
print(tinyDict.values())

shopDict = dict([('taobao', 1), ('tianmao', 2), ('jingdong', 3)])
print(shopDict)
a = 20
b = 20
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