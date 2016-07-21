#!/usr/bin/env python
# coding=utf-8

while True:
    s = 0
    c = int(input('1.sum\n2.ave\n3.exit\ninput num:'))
    print

    if c == 3:
        break
        
    for i in range(5):
        n = int(input('n%d=' % (i+1)))
        s += n

    if c == 1:
        print s
    if c == 2:
        print float(s / 5)
