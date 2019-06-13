# -*- coding: utf-8 -*-
from multiprocessing import Pool, Process, Queue
import os, time, random, subprocess


def long_time_task(name):
    print('执行 {} 任务，pid：{}'.format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('任务 %s 执行了 %0.3f seconds' % (name, (end - start)))

if __name__ == '__main__':
    print('父进程号：<{}>'.format(os.getpid()))
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('等待所有子线程执行结束')
    p.close()
    # 对pool 对象调用join方法会等待所有子进程执行完毕，调用join方法之前必须先调用池的close方法，调用close方法之后就不能添新的进城了
    p.join()
    # 这里由于我是双核四线程的机器，所以0，1，2，3是同时执行完的，而4是等前面执行完才获取到cpu资源执行的
    print('所有子线程执行结束')

# 控制子进程的输入输出
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('exit code', r)

# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('exit code', p.returncode)

# 进程间通信，可以使用queue、pipes等多种方式来交换数据
# 写数据进程执行的代码


def write(q):
    print('写进程：{}'.format(os.getpid()))
    for value in ['a', 'b', 'c']:
        print('将 {} 放到队列 '.format(value))
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('读进程：{}'.format(os.getpid()))
    while True:
        value = q.get(True)
        print('从队列获得数据{}'.format(value))


if __name__ == '__main__':
    # 父进程创建queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))
    pw.start()
    pr.start()
    pw.join()
    # 读进程是死循环，需要强行终止
    pr.terminate()