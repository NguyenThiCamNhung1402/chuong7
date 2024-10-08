# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 19:06:43 2024

@author: Student
"""

import math
def tinh(*args, **kwargs):
    hinh = kwargs.get('hinh')
    tinh = kwargs.get('tinh')
    if hinh == 'vuong':
        canh = args[0]
        return 4 * canh if tinh == 'cv' else canh ** 2
    elif hinh == 'tron':
        bk = args[0]
        return 2 * math.pi * bk if tinh == 'cv' else math.pi * bk ** 2
    elif hinh == 'chu_nhat':
        dai, rong = args
        return 2 * (dai + rong) if tinh == 'cv' else dai * rong
    else:
        return "Hình không hợp lệ"
if __name__ == "__main__":
    print(tinh(10, hinh='vuong', tinh='cv')) 
    print(tinh(50, hinh='vuong', tinh='dt'))  
    print(tinh(18, hinh='tron', tinh='cv'))  
    print(tinh(20, 30, hinh='chu_nhat', tinh='cv'))  