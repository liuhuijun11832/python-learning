# -*- coding: utf-8 -*-
import socket

# 客户端
# 创建socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
# s.connect(('www.guitar-coder.cn', 80))
s.connect(('127.0.0.1', 9999))

# 发送数据:
# s.send(b'GET / HTTP/1.1\r\nHost: www.guitar-coder.cn\r\nConnection: close\r\n\r\n')

# 接收数据
# buffer = []
# while True:
#     # 每次最多接收1k
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# # 断开连接
# s.close()
# header, html = data.split(b'\r\n\r\n', 1)
# with open('my.html', 'wb') as f:
#     f.write(html)
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Joy', b'Starck']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))

s.send(b'exit')
s.close()