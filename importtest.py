# -*- coding: utf-8 -*-
# 导入一个模块的某个方法，import *代表所有方法（但是_开头的名字不在此列），同时被导入模块中的可执行代码在第一次也会执行
from MyNumbers import printme
import math
import pickle
import pprint

printme("哈哈哈哈哈哈")


"""dir函数可以找到模块内定义的所有名称，以一个字符串列表的形式返回,如果没有参数，那就是当前模块"""
print(dir())

"""当使用from package import item这种形式的时候，对应的item既可以是包里面的子模块（子包），或者包里面定义的其他名称，比如函数，类或者变量"""
"""如果使用形如import item.subitem.subsubitem这种导入形式，除了最后一项，都必须是包，而最后一项则可以是模块或者是包，但是不可以是类，函数或者变量的名字"""

print('{}和{}'.format("google", "alibaba"))
print('{1}和{0}'.format("google", "alibaba"))
print('{site}和{url}'.format(site="google", url="http://www.google.com"))
print('常量PI的值近似为{0:.3f}'.format(math.pi))


str = input("请输入：")
print("你输入的内容是：",str)


"""打开文件的模式：
r：默认，只读，从文件头开始
rb：只读，文件头，二进制
r+：读写，文件头开始
w：只写，文件头，覆盖，新建
wb：只写，文件头，覆盖新建，二进制
w+：读写，文件头，覆盖，新建
a：追加，新建
ab：二进制追加，新建
a+：读写，追加，新建
ab+：二进制读写，追加，新建
"""

# 文件的只写
f = open("E:\\test.txt", "w")
f.write("python 是一个非常好的语言。 \n是的，的确非常好\n")
# 返回文件对象当前所处的位置，它是从文件头开始算起的字节数
print(f.tell())
# 能够改变文件当前的位置，第一个参数为移动多少位，如果第二个参数时0表示文件开头，为1表示当前位置，为2表示文件结尾
f.seek(5, 0)
f.close()


# 文件的只读
r = open("E:\\test.txt", "r")
tmpStr = r.readline()
print(tmpStr)
tmpEntityStr = r.readlines()
print(tmpEntityStr)
r.close()


# pickle模块实现了基本的数据序列化和反序列化
# 将数据保存到文件
data1 = {'a': [1, 2, 3, 4, 5*6], 'b': ('string', u'Unicode String'), 'c': None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
# x = pickle.load(selfref_list)
output = open('E:\\data.pkl', 'wb')
pickle.dump(data1, output)
pickle.dump(selfref_list, output, -1)
output.close()

# 从文件中重构python对象
pkl_file = open('E:\\data.pkl', 'rb')
data2 = pickle.load(pkl_file)
pprint.pprint(data2)

data3 = pickle.load(pkl_file)
pprint.pprint(data3)
pkl_file.close()