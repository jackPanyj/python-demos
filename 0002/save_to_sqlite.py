#!/usr/bin/env python
# -*-coding:utf-8-*-

# 第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

def create_table():

    cursor.execute('create table if not exists code ( id INTEGER PRIMARY KEY AUTOINCREMENT, random_code varchar(10))')

    conn.commit()



def save_to_sqlite():

    f = open('../0001/code.txt', 'r')

    s = ''

    #拼接sql

    for line in f.readlines():

        s = s + "('{0}'),".format(line)

    cursor.execute('insert into code (random_code) values' + s.rstrip(',')) 

    conn.commit()


if __name__ == '__main__':

    create_table()

    save_to_sqlite()

    cursor.close()

    conn.close()