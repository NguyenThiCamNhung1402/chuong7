# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:35:31 2024

@author: Student
"""

def chu_vi(a,b):
    return (a+b)*2
def dien_tich(a,b):
    return a*b
def ve_hcn(a,b):
    for i in range(a):
        print('*' * b)
if __name__=="__main__":
    print(chu_vi(3,8))
    print(dien_tich(3,8))
    print(ve_hcn(3,8))     