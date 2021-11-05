#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Проверка на простое число

def main():
    x=int(input('Введите число: '))
    i=1
    flag=0
    
    while i<(x-1):
        i+=1
        if (x%i)==0:
            flag=1
    
    if flag==0:
        print('Число простое')
    else:
        print('Число не простое')
    
if __name__=="__main__":
    main()

