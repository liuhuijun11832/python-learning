# -*- coding: utf-8 -*-
from multiprocessing import Process
import os
'''多线程相关内容'''

print('process (%s) start ...'% os.getpid())
# 以下代码只能运行于非windows平台
# pid = os.fork()
#
# if pid == 0:
#     print("子进程永远返回0，该进程pid为 (%s)"% os.getpid())
# else:
#     print("父进程（%s）刚刚创建了一个子进程（%s）"% (os.getpid(), pid))


def run_proc(name):
    print("运行子进程 {} ({})".format(name, os.getpid()))
if __name__ == '__main__':
    print('父进程:{}'.format(os.getpid()))
    p = Process(target=run_proc, args=('test',))
    print('子进程即将启动')
    p.start()
    p.join()
    print('子进程启动结束')




