# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:13:27 2024

@author: Student
"""
import math 
def can_bac_x(x,n):
    return x**(1/n)
def so_dao(x):
    return 1/x
def chinh_phuong(n):
    return math.sqrt(n) ==int(math.sqrt(n))
def nguyen_to(n):
    if n <= 1:
        return "Không là số nguyên tố"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Không là số nguyên tố"
    return "Là số nguyên tố"
def tich_so_le(*args):
    tich=1 
    so_le= False 
    for i in args:
        if i %2 !=0:
            so_le= True
            tich*= i
        return tich 
if __name__=="__main__":
    ds=[1,3,5,7]
    print(can_bac_x(4,2))
    print(so_dao(9473))
    print(chinh_phuong(4))
    print(nguyen_to(2))
    print(tich_so_le(*ds))