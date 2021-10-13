# -*- coding: utf-8 -*-


# 2.Matrix multiplication
# 2.1
import numpy as np
M1 = np.random.randint(0,50,[5,10])
M2 = np.random.randint(0,50,[10,5])
# 2.2
def Matrix_multip(M1,M2):
    list1 = []
    res = []
    for i in range(0, len(M1[:,0])):
        A = M1[i,:]
        for j in range(0, len(M2[0,:])):
            B = M2[:,j]
            B = B.reshape(1,-1)
            C = A*B
            D = sum(C[0])
            list1.append(D)
        a = np.asarray(list1).reshape(1,-1)
        res.append(a[0])
        list1 = []
    res = np.asarray(res)
    print(res)
    return

if __name__ == "__main__":
    res=Matrix_multip(M1, M2)