#!/usr/bin/env python
# coding=utf-8

import numpy as np
from scipy.stats import expon
import matplotlib.pyplot as plt

y = []
n = 1000

for i in range(10000):
    r = expon.rvs(scale=1,size=n)#mu=1
    rsum = np.sum(r)
    y.append(rsum)

plt.hist(y,100,color='grey')
plt.show()
