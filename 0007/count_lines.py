#!/usr/bin/python
#coding:utf-8

"""第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。"""

import glob2,os

def save_to_dic(k, dic):
    '''检测dic是否有k，如果有其值加1，否则设置为1'''
    if k in dic:
        dic[k] += 1
    else:
        dic[k] = 1

def count_lines(file_names):
    '''遍历文件对象，根据特征判断注释，空行跟代码然后依次写入dic中'''
    for file_name in file_names:
        with open(file_name) as f:
            dic = {}
            lines = f.readlines()
            for line in lines:
                strip_line = line.strip()
                save_to_dic('total_lines', dic) # 总行数
                if len(strip_line) == 0:
                    save_to_dic('empty_lines', dic) # 空行
                elif strip_line.startswith('"""') or strip_line.startswith('#') or strip_line.startswith('\'\'\''):
                    save_to_dic('note_lines', dic) # 注释行
                else:
                    save_to_dic('code_lines', dic) # 代码行
            print file_name, dic

if __name__ == '__main__':
    file_names = glob2.glob('../00*/**/*.py')
    count_lines(file_names)