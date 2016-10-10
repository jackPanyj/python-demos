#!/usr/local/bin/python
#coding=utf-8

"""
第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
"""
from PIL import Image
import glob, os


def transform_img(path, width, height):
    imgs = glob.glob(path)
    for img in imgs:
        name, ext = os.path.splitext(img)
        with Image.open(img) as im:
            # 按照图片的比例缩小
            w, h = im.size
            rate = w / float(h)
            if (w > width):
                w = width
                h = int(w / rate)
            if (h > height):
                h = height
                w = int(h * rate)

            im_resize = im.resize((w, h))
            im_resize.save('{0}.thumail{1}'.format(name, ext))


if __name__ == '__main__':
    width = 640
    height = 1136
    path = 'imgs/*'
    transform_img(path, width, height)