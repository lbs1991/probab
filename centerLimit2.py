#!/usr/bin/env python
# coding=utf-8

import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt

y = []
n = 1000

for i in range(10000):
    r = binom.rvs(n,0.3)
    rsum = np.sum(r)
    #z = (rsum-n*0.3)/np.sqrt(n*0.3*0.7)
    #y.append(z)
    y.append(rsum)

plt.hist(y,100,color='grey')
plt.show()
