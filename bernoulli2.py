#!/usr/bin/env python
# coding=utf-8

import  numpy as np
import matplotlib.pyplot as plt
from scipy.stats import *

if __name__ == '__main__':
    x = np.arange(1,10001,1)
    r1 = binom.rvs(10,0.6,size=10000)
    r2 = poisson.rvs(mu=6, size= 10000)
    r3 = norm.rvs(loc=6,size=10000)

    y = []
    rsum = 0.0
    for i in range(10000):
        rsum = rsum+(r1[i]+r2[i]+r3[i])
        y.append(rsum/((i+1)*3)-6)

    plt.plot(x,y,color='red')
    plt.show()
