#!/usr/bin/env python
# -*-coding:utf-8-*-

# 第 0003 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。

import redis

def init_redis():
    return redis.Redis(host = 'localhost', port = 6379, db = 1)

def save_to_redis():
    with open('../0001/code.txt') as f:
        r = init_redis()
        [r.lpush('code', line) for line in f.readlines()]

def get_from_redis():
    r = init_redis()
    for code in r.lrange('code', 0, -1):
        print code.strip()

if __name__ == '__main__':
    save_to_redis()
    get_from_redis()