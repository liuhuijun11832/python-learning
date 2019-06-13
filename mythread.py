# -*- coding: utf-8 -*-
import time, threading
'''python的标准库内置了两个模块，_thread和threading，前者是低级模块，后者是高级模块，一般情况下，使用高级模块'''


def loop():
    print('线程正在运行：{}'.format(threading.current_thread().name))
    n = 0
    while n < 5:
        n += 1
        print('线程 {} >>> {}'.format(threading.current_thread().name, n))
        time.sleep(1)
    print('线程 {} 结束'.format(threading.current_thread().name))

print('线程{}正在运行...'.format(threading.current_thread().name))
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join( )
print('线程 {} 结束'.format(threading.current_thread().name))

'''线程和进程最大的区别在于：进程中的同一变量是拷贝存放于每个进程中，互不影响；而多线程中，所有变量由所有线程共享，所以通常需要加一把锁'''
# 假如这是银行存款
balance = 0
lock = threading.Lock()


def change_it(n):
    # 先存后取，结果为0
    global balance
    balance += n
    balance -= n


def run_thread(n):
    for i in range(100000):
        # 首先要获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 还需要释放锁
            lock.release()


# python中会有Gil锁，然后每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行，所以python只能利用到一个核，然后多线程交替执行
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

# 线程安全的本地变量，
local = threading.local()
