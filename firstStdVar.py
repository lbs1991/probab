#!/usr/bin/env python
# coding=utf-8

from thinkstats import *
from first import *

def Main(data_dir='.'):
    table,firsts,others = MakeTables(data_dir)
    ProcessTables(firsts, others)
    fVar = Var(firsts.lengths)
    oVar = Var(others.lengths)
    print "first babies var is ",fVar
    print "others babies var is ",oVar

if __name__ == '__main__':
    Main()
