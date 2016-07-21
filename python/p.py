#!/usr/bin/env python
# coding=utf-8

class a:
    version = 0.1
    def __init__(self,nm="asdf"):
        self.name = nm
    def show(self):
        print "111"
        print self.version
        print self.__class__.__name__
        

s = a()
s.show()
s1 = a('ruixin')
s1.show()

import ppp
ppp.func()
