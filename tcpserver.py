# -*- coding: utf-8 -*-
import socket, threading, time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 使用元组传参数
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('waiting for connection...')


def tcplink(sock, addr):
    print('accept new connection from {}'.format(addr))
    sock.send(b'welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send('hello , {}'.format(data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('connection from {} closed'.format(addr))

while True:
    socket, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(socket, addr))
    t.start()