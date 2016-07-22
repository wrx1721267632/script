#!/usr/bin/env python
# coding=utf-8

import random
import redis

num = []
for i in range(100):
    num.append(random.randint(1,1000))
print num
r = redis.StrictRedis(host = 'localhost',port = 6379, db = 3)
r.set('dssd','ss')
for i,x in enumerate(num):
    r.set(i,x)
print '添加成功'
newnum = [r.get(i) for i in range(100)]
print newnum
