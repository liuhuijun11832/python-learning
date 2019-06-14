# -*- coding: utf-8 -*-
import asyncio, threading


# 把一个generator标记为coroutine类型，然后扔到EventLoop中执行
# @asyncio.coroutine
# def hello():
#     print('hello world')
#     # yield from可以让我们方便地调用另外一个generator
#     r = yield from asyncio.sleep(1)
#     print('hello again')
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()


'''模拟两个任务同时进行，可以看到两个coroutine是并发执行的'''
# @asyncio.coroutine
# def hello1():
#     print('hello world %s' % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('hello again %s' % threading.currentThread())
#
# loop1 = asyncio.get_event_loop()
# tasks = [hello1(), hello1()]
# loop1.run_until_complete(asyncio.wait(tasks))
# loop1.close()


# @asyncio.coroutine
# def wget(host):
#     print('wget %s=====' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET /HTTP/1.0 \r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     writer.close()
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


'''python 3.5引入了新的语法async和await,使得coroutine的代码更简洁易读'''
async def hello1():
    print('hello world %s' % threading.currentThread())
    await asyncio.sleep(1)
    print('hello again %s' % threading.currentThread())

loop1 = asyncio.get_event_loop()
tasks = [hello1(), hello1()]
loop1.run_until_complete(asyncio.wait(tasks))
loop1.close()