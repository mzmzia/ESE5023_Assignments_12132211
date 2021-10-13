# -*- coding: utf-8 -*-
# """

# @author: Potatomato
# """

# Method 
# 5.1
import numpy as np
A = np.random.randint(1,101)
def Find_expression(A : int,nums: str) -> list:
    opra = ['+', '-', '']
    def find_all(nums: str) -> list:
        if len(nums) == 1:
            return [nums] 
        else:
            return [nums[0] + j + i for i in find_all(nums[1:]) for j in opra]
    return [k+'='+str(A) for k in find_all(nums) if eval(k) == A]

if __name__ == "__main__":
    results = Find_expression(A,"123456789")
    # 验算式子结果
    # for result in results:
    #     assert eval(result) == A
    print("Done")
    
# --------------------------------------------------------------------  
# 5.2  
Toal_solutions=[]
for i in range(1,101):
    solutions = Find_expression(i, "123456789")
    # 验算式子结果
    # for result in solutions:
    #     assert eval(result) == i
    print("solutions of number: "+str(i)+" have Done")
    Toal_solutions.append(solutions)



maximum=max(len(max_elem) for max_elem in Toal_solutions)
minimum=min(len(mini_elem) for mini_elem in Toal_solutions)