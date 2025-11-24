# -*- coding: utf-8 -*-
from functools import reduce
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is {self.age} years old")

d = Dog("heoy", 11)
d.sit()

def add(number):
    return number + number

## map(函数,可迭代对象)
range(5)
map(add, range(5))
for i in map(add, range(5)):
    print(i)

print(list(map(add, range(5))))
print(list(map(lambda x: x **2, range(5))))

## filter(函数, 可迭代对象)
for e in filter(lambda x: x % 2 == 0, range(5)):
    print(e)


## reduce(函数，可迭代对象，类比)
from functools import reduce
print(reduce(lambda x,y: x+ y,[1,2,3,4,5]))

## 进制转换-偏函数
from functools import partial
print(int('0f', base=16))
int_16 = partial(int, base=16)
print(int_16('0f'))
