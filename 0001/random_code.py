#!/usr/bin/env python
# -*-coding:utf-8-*-

import uuid

'''第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？'''
def random_code():
	f = open('./code.txt', 'w')

	for i in range(200):
		s = str(uuid.uuid4())[0:8]
		f.write(s + '\n')
	f.close()


if __name__ == '__main__':
	random_code()
