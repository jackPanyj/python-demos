#!/usr/bin/env python
# -*-coding:utf-8-*-

'''第 0008 题：一个HTML文件，找出里面的正文。'''
from bs4 import BeautifulSoup
import os

def get_body_and_href():
    os.system('curl -o baidu.html www.baidu.com')
    with open('baidu.html') as f:
        soup = BeautifulSoup(f, 'html.parser')
        print(soup)
        print(soup.find_all('a'))

if __name__ == '__main__':
    get_body_and_href()