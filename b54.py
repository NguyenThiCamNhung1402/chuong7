# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:20:39 2024

@author: Student
"""

def fib(n):
     a,b=0,1
     while a<n:
         print(a,end=' ')
         a,b=b,a+b
if __name__=="__main__":
    print(fib(2018))