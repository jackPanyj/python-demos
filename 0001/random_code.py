#!/usr/bin/env python
# -*-coding:utf-8-*-

import uuid

'''第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？'''
def random_code():
	codes = list()
	for i in range(200):
		# 避免出现伪随机数重复
		while True:
			code = str(uuid.uuid4())[0:8]
			if code not in codes:
				break
		codes.append(code)
	# 使用with语法自动处理，写入完成自动关闭文件
	with open('./code.txt', 'w') as f:
		f.writelines(codes)

if __name__ == '__main__':
	random_code()
