# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 18:11:43 2024

@author: Student
"""
import random
def tao_seqA():
    seqA=[]
    n=random.randint(30,80)
    for i in range(n):
        if random.randint(0,1)==0:
            seqA.append(round(random.uniform(-79,39),2))
        else:
            seqA.append(random.randint(-79,39))
    return seqA
def ktra_dulieu(seqA):
    return [type(i).__name__ for i in seqA]
def thongke(seqA):
    return len(seqA)
def sapxep_seqB(seqA):
    return sorted(seqA)
def trungbinh(seqA):
    return sum(seqA)/len(seqA)
def trungbinh_seqB(seqB):
    n= len(seqB)
    if n%2==0:
        return (seqB[n//2-1]+seqB[n//2])/2
    else:
        return seqB[n//2]
def khoangcach(seq):
    return max(seq)-min(seq)
def sosanh(seqA,seqB):
    return trungbinh(seqA),trungbinh_seqB(seqB), trungbinh(seqA)==trungbinh_seqB(seqB)
if __name__=="__main__":
    seqA=tao_seqA()
    print(seqA)
    print(ktra_dulieu(seqA))
    print(thongke(seqA))
    seqB=sapxep_seqB(seqA)
    print(seqB)
    print(trungbinh(seqA))
    print(trungbinh_seqB(seqB))
    print(khoangcach(seqA))
    print(khoangcach(seqB))
    sosanh_AB=sosanh(seqA,seqB)
    print(sosanh_AB)
    
