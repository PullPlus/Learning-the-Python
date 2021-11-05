#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Вычисление корня

def main():
    x=float(input('Введите число: '))
    y=float(input('Введите степень корня: '))
    z=100 #float(input('Введите количество итераций:'))
    i=0
    a=x/y
    
    while i<z:
        a=(1/y)*((y-1)*a+(x/(a**(y-1))))
        i+=1
    
    print('Приближенный корень: ',a)

if __name__=="__main__":
    main()

