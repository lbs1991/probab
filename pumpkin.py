#!/usr/bin/env python
# coding=utf-8

from  thinkstats import MeanVar

def Pumpkin():
    weight = [1,1,1,3,3,591]
    mu , var = MeanVar(weight)
    print "the pump mu is " ,mu 
    print 'var is ' , var

if __name__ == '__main__':
    Pumpkin()
