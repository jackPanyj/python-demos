#! /usr/bin/en python
# coding:utf-8

import tinify
import glob
import os

''' 利用tinypng的api对指定的目录进行图片的压缩 '''

KEY = 'APP_KEY'

def minImg(src_dir, des_dir):
    ''' 将路径转换为绝对路径 '''
    src_path = os.path.abspath(src_dir)
    des_path = os.path.abspath(des_dir)
    
    ''' 调用tinypng的api压缩目录下面的所有的png '''
    tinify.key = KEY
    arr_png = glob.glob(f'{src_path}/*.png')
    for src in arr_png:
        basename = os.path.basename(src)
        source = tinify.from_file(src)
        source.to_file(f'{des_path}/{basename}')

if __name__ == '__main__':
    minImg('imgs', 'imgs_min')
