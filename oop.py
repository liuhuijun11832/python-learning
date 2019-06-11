# -*- coding: utf-8 -*-


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