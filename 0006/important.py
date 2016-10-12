#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第 0006 题：你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

from glob2 import glob
import re, os

# 统计单词数量
def find_hot(words):
    word_dict = {}
    for word in words:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return str(sorted(word_dict.items(), key=lambda e: e[1], reverse=True))

# 打印列表
def print_hot_word(file_names):
    for file_name in file_names:
        with open(file_name) as f:
            word_list = re.findall('[a-zA-Z1-9]+', f.read())
            print file_name + ': ' + find_hot(word_list)

if __name__ == '__main__':
    file_names = glob('txt/**/*.txt')
    print_hot_word(file_names)