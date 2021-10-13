# -*- coding: utf-8 -*-


import numpy as np
x = np.random.randint(1,100)
n = x
i = 0
while n > 1:
    i +=1
    if (n%2) == 0:
        n = n/2
    else:
        n = (n-1)/2
        i +=1
print(i)