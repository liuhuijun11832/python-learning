# -*- coding:utf-8 -*-
import mysql.connector, logging

conn = mysql.connector.connect(host='94.191.72.116', user='root', password='liuhuijunroot..', database='blog')
cursor = conn.cursor()
cursor.execute('create table if not exists user (id integer primary key auto_increment, name varchar(20))')
logging.basicConfig(level=logging.INFO)
logging.info('insert into user(`id`,`name`) values ({}, "{}")'.format(3, 'Joy'))
cursor.execute('insert into user(`id`,`name`) values ({}, "{}")'.format(3, 'Joy'))
print(cursor.rowcount)
conn.commit()
cursor.close()
cursor = conn.cursor()
cursor.execute('select * from user')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()