# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 19:42:20 2024

@author: Student
"""
def sum1(n):
    s=0
    for i in range(1,n+1):
        s+=i
    return s
def sum2(n):
    s=0 
    for i in range(1,n+1):
        s+=i**2
    return s
def sum3(n):
    s=0
    for i in range(1,n+1):
        s+=1/i
    return s
def giai_thua(n):
    if n==0 or n==1:
        return 1
    kq=1
    for i in range(2,n+1):
        kq*=i
    return kq   
def sum4(n):
    s=0
    for i in range(1,n+1):
        s+=giai_thua(i)
    return s
def sum5(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s
if __name__=="__main__":
    print(sum1(5))
    print(sum2(3))
    print(sum3(3))
    print(sum4(3))
    print(sum5(4))

