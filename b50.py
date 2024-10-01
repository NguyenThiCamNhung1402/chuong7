# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:03:16 2024

@author: Student
"""

def ktr(x):
    if x<0 and x%2!=0:
        return -1
    elif x>0 and x%2==0:
        return 1
    else:
        return 0
if __name__=="__main__":
    print(ktr(6))