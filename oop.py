# -*- coding: utf-8 -*-

import types
import logging


class MyClass:
    # 一个简单的类实例
    i = 12345

    def f(self):
        return 'hello world'

    def __init__(self):
        print("执行了MyClass的init方法")


# 实例化类,会调用init方法
x = MyClass()

# 访问类的属性和方法
x.i
x.f()

"""self代表类的实例，而不是类"""


class FirstClass:
    def prt(self):
        # self指向了当前实例的地址
        print(self)
        # slef.class则指向类
        print(self.__class__)


first = FirstClass()
first.prt()
"""这个slef不是关键字，换成其他参数也是一样的"""


class SecondClass:
    def prt(me):
        print(me)
        print(me.__class__)


second = SecondClass()
second.prt()
"""类的方法：类的方法第一个参数必须是类的实例"""


class People:
    name = ''
    age = 0
    # 定义私有属性，外部无法直接访问
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w;

    def speak(self):
        print("{}说：我{}岁".format(self.name, self.age))


p = People("liu hui jun", 25, 33)
p.speak()
"""类的继承，如果没有继承，那么类的存在也就没有了意义"""


class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的init
        People.__init__(self, n, a, w)
        self.grade = g

    # 重写父类方法
    def speak(self):
        print("{}说：我{}岁，我在读{}年纪".format(self.name, self.age, self.grade))


s = Student("joy", 10, 80, '三')
s.speak()


class Speaker:
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫{}，我是一个演说家，我演讲的主题是{}".format(self.name, self.topic))
"""多继承，当调用子类继承过来的方法时，会按照继承的顺序前后找"""


class Sample( Speaker, Student):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)
test = Sample('tim', 25, 80, 4, 'Java')
test.speak()
"""方法重写"""


class Parent:
    def mymethod(self):
        print("调用父类方法")


class Child(Parent):
    def mymethod(self):
        print("调用子类方法")


a = list()
b = Parent()
c = Child()

print(isinstance(a, list))
print(isinstance(b, Parent))
print(isinstance(c, Child))
# 继承过来的也可以时父类型 所以下面语句是True
print(isinstance(c, Parent))

"""判断一个对象是否是函数，可以使用types模块中定义的常量"""

print("=========函数类型比较=======")


def fn():
    pass
# 优先使用isinstance()来判断，因为type无法比对继承下来的类类型
# true
print(type(c) == Child)
# false
print(type(c) == Parent)
print(type(fn) == types.FunctionType)
print(isinstance(fn, types.FunctionType))
print(type(abs) == types.BuiltinFunctionType)
print(isinstance(abs, types.BuiltinFunctionType))


# 还可以判断一个变量是否是某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

"""类似__xxx__的属性和方法在python内部中都是由特殊用途的，例如__len__方法返回长度，如果使用len（）函数试图获取一个对象的长度，在len()内部会自动调用对象的__len__()方法"""
"""自己写的类，如果也想用len方法，可以自己写一个__len__()"""


class MyObject(object):

    def __init__(self):
        self.x = 9

    def powef(self):
        return self.x * self.x

'''可以通过getattr()或者setattr()等一系列的方法来获得属性，但是只有在不知道对象信息的时候，才使用getattr()或者setattr()等方法，优先使用obj.x的方式来代替getattr(obj,'x')
的方式'''
obj = MyObject()
hasattr(obj, 'x')
hasattr(obj, 'y')
print(getattr(obj, 'x'))
setattr(obj, 'y', 18)
print(obj.y)


# 使用slots变量可以声明一个元组，元组里的元素是允许绑定的属性名称
# _score变量做了限制，使得其无法随心所欲
class Student(object):
    # __slots__ = ('name', 'age')

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = value

s = Student()
s.name = 'Joy'
s.age = 24
s.set_score(90)

# 但是有更简单的方法对变量做限制：@property，把一个getter方法变成属性，就是加上@property注解；把一个setter方法变成属性赋值就是加上@属性.setter。
# 如果是只读属性，就不需要@属性.setter了


class Student1(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = value
s1 = Student1()
s1.score = 90

'''定制类'''
# 定制__str__


class Human(object):
    def __init__(self, name):
        self.name = name
    # __str__能够自定义返回用户看到的字符串

    def __str__(self):
        return 'Human object (name: {})'.format(self.name)
    # __repr__返回给程序开发者看到的字符串
    __repr__ = __str__

# print(Human('Joy'))
h = Human('Joy')
print(s)

# 定制__iter__


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000000:
            raise StopIteration
        return self.a

    # 定制__getitem__ ,使其能够像list一样根据下标取数据
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a

    # 定制__getattr__ __getattr__这个方法只有在没某个变量的时候才会调用
    def __getattr__(self, item):
        if item == 'age':
            return lambda: 25

for n in Fib():
    print(n)

f = Fib()
print(f.age())


# 定制__call__: 这样直接调用一个实例，就和调用一个对象一样。函数和对象本身没有什么根本的区别


class Student3():
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print("my name is {}".format(self.name))

s3 = Student3('Joy')
s3()


# assert isinstance('dd', int), '数据不是整型'

logging.basicConfig(level=logging.INFO)
logging.info("决定离开房间了dj")
logging.debug("fjdalsjfl")

