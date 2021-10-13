# -*- coding: utf-8 -*-


# 1.Flowchart
def Print_values(a,b,c):
    if a>b:
        if b>c:
            result = print(a,b,c)
        else:
            if a>c:
                result = print(a,c,b)
            else:
                result = print("NaN")
    else:
        if b>c:
            if a>c:
                result = print(b,a,c)
            else:
                if b>c:
                    result = print(b,c,a)
                else:
                    result = print(c,b,a)
        else:
            result = print(c,b,a)
    return result