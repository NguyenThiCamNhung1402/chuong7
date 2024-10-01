# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:05:35 2024

@author: Student
"""

def ktr():
    x= input("Nhập một giá trị:")
    if x.replace(".","",1).replace("-","",1).isdigit():
        x=float(x)
    if -89<= x<=90:
        return x
    print("Không hợp lệ. Nhập lại:")
    return ktr()
if __name__=="__main__":
    print(ktr())