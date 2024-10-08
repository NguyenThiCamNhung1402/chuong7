# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:13:27 2024

@author: Student
"""
import math 
def can_bac_x(x,n):
    return x**(1/n)
def so_dao(n):
    str_n = str(n)
    dao_chuoi = str_n[::-1]
    if dao_chuoi[0] == '0':
        return dao_chuoi  
    else:
        return int(dao_chuoi)
def chinh_phuong(n):
    return math.sqrt(n) ==int(math.sqrt(n))
def nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def tich_so_le(*args):
    tich=1 
    for i in args:
        if i %2 !=0:
            tich*= i
        return tich 
def sum_nguyen_to(a):
    tong = 0
    for i in range(2, a):
        if nguyen_to(i):
            tong += i
    return tong
def sum_chinh_phuong(x):
    kq=0
    for i in range(1,x):
        if chinh_phuong(i):
            kq+=i
    return kq
def sum_uoc_duong(n):
    S = 0
    for i in range(1, n + 1):  
        if n % i == 0:  
            S += i  
    return S
if __name__=="__main__":
    ds=[1,3,5,7]
    print(can_bac_x(4,2))
    print(so_dao(9470))
    print(chinh_phuong(4))
    print(nguyen_to(2))
    print(tich_so_le(*ds))
    print(sum_nguyen_to(10))
    print(sum_chinh_phuong(10))
    print(sum_uoc_duong(10))

