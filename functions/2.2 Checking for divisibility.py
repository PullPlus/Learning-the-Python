#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Проверка на делимость

def triple_kill(l0=[]):
    l2=[]
    l3=[]
    l5=[]
    while l0:
        i=int(l0.pop(0))
        if (i%2)==0 and i>0:
            l2.append(i)
        if (i%3)==0 and i>0:
            l3.append(i)
        if (i%5)==0 and i>0:
            l5.append(i)
    l0.append(l2)
    l0.append(l3)
    l0.append(l5)
    return l0

def main():
    list=input('Ведите список чисел, через пробел: ').split()
    #list=[1,2,3,4,5,6,7,8,9,0]
    list=triple_kill(list)
    print(list)

if __name__=="__main__":
    main()
