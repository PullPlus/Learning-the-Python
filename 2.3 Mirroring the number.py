#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Зеркалирование числа

def reverse_int(X):
    Y=0
    while X:
        Y=Y*10+X%10
        X=X//10
    return Y

def main():
    x=int(input('Ведите зеркалируемое число: '))
    print(reverse_int(x))

if __name__=="__main__":
    main()

