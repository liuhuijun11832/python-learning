# -*- coding: utf-8 -*-
import os
import json

print(os.path.abspath("."))

'''在某个目录下创建一个新目录，首先把新目录的完整路径表示出来'''
print(os.path.join("E:\\PycharmProjects\\python-learning", "testdir"))
'''真正的创建'''
# os.mkdir("E:\\PycharmProjects\\python-learning\\testdir")
'''删除一个目录'''
# os.rmdir("E:\\PycharmProjects\\python-learning\\testdir")


'''操作系统中的环境变量都在os.environ中'''
print(os.environ.get('PATH'))

'''把路径拆成两部分使用os.path.split'''
print(os.path.split(r"E:\PycharmProjects\python-learning"))

d = dict(name='Bob', age=20, score=90)
print(json.dumps(d))
json_str = '{"name": "Bob", "age": 20, "score": 90}'
print(json.loads(json_str))


class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

# 专门用于转换student的函数


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Joy', 20, 88)
# 对于自定义的类，无法被序列化，这时我们可以使用序列化的default属性调用专属函数进行序列化
print(json.dumps(s, default=student2dict))
# 将也可以采取这种偷懒的办法，将自定义的类先转成dict类型
'''因为通常一个class的实例都会有一个__dict__属性，它就是一个dict，用来存储实例变量，除非是定义了__slots__的class'''
print(json.dumps(s, default=lambda obj: obj.__dict__))
json_str = '{"name":"Joy","age":18,"score":90}'
'''同理，还需要一个函数进行反序列化'''


def dict2student(stdin):
    return Student(stdin['name'], stdin['age'], stdin['age'])
print(json.loads(json_str, object_hook=dict2student))