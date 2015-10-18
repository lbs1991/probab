#!/usr/bin/env python
# coding=utf-8

"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import first
import math
import Pmf
import survey
import thinkstats



def Process(table, name):
    """Runs various analyses on this table."""
    first.Process(table)
    table.name = name

    table.var = thinkstats.Var(table.lengths, table.mu)
    table.trim = thinkstats.TrimmedMean(table.lengths)

    table.hist = Pmf.MakeHistFromList(table.lengths, name=name)
    table.pmf = Pmf.MakePmfFromHist(table.hist)
        
        
def PoolRecords(*tables):
    """Construct a table with records from all tables.
    
    Args:
        constructor: init method used to make the new table
    
        tables: any number of tables

    Returns:
        new table object
    """
    pool = survey.Pregnancies()
    for table in tables:
        pool.ExtendRecords(table.records)
    return pool


def MakeTables(data_dir='.'):
    """Reads survey data and returns a tuple of Tables"""
    table, firsts, others = first.MakeTables(data_dir)
    pool = PoolRecords(firsts, others)

    Process(pool, 'live births')
    Process(firsts, 'first babies')
    Process(others, 'others')
        
    return pool, firsts, others

def Probility(pmf,peroid):
    prob = 0
    for pd,pb in pmf.d.iteritems():
        print pd,pb
        if int(pd)<=peroid :
            prob += pb
    print prob
    return prob

def ProbEarly(pmf):
    prob = Probility(pmf,37)
    return prob

def ProbOnTime(pmf):
    prob1 = Probility(pmf,37)
    prob2 = Probility(pmf,40)
    prob = prob2 - prob1
    return prob

def ProbLate(pmf):
    prob1 = Probility(pmf,40)
    prob = 1.0 - prob1
    return prob

def main(name, data_dir=''):
    pool, firsts, others = MakeTables(data_dir)
    fpe = ProbEarly(firsts.pmf)
    ope = ProbEarly(others.pmf)

    print 'first babies born early is ' ,fpe
    print 'others babies born early is ' ,ope

if __name__ == '__main__':
    import sys
    main(*sys.argv)


