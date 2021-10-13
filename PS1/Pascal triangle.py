# -*- coding: utf-8 -*-
# import pandas as pd
numRows = 200
# 3. Pascal triangle
# def generate(numRows: int):
# if numRows == 0:# return []
res = [[1]]
while len(res) < numRows:
    newRow = [a+b for a, b in zip([0]+res[-1], res[-1]+[0])]
    res.append(newRow)      
print(res[numRows-1])
# return res






## report
# save
# test = pd.DataFrame(data = res)
# print(test)
# test.to_csv('c:/Users/Potatomato/Desktop/testdata2.csv',encoding = 'gbk')