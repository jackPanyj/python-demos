#!/usr/bin/env python
# -*-coding:utf-8-*-


# 第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数
import os
import re

# 利用str.split()来分割单词
def method1(file_path):
    with open(file_path, 'r') as f:
        print len(f.read().split())

# 利用bash的命令` wc -w english.txt `来统计单词数量
def method2(file_path):
    print os.popen('wc -w {0}'.format(file_path)).read()

# 利用正则表达式来统计数量
def method3(file_path):
    with open(file_path, 'r') as f:
        words = re.findall(r'[a-zA-Z0-9]+', f.read())
        print len(words)

if __name__ == '__main__':
    file_path = 'english.txt'
    method1(file_path) 
    method2(file_path)
    method3(file_path)
