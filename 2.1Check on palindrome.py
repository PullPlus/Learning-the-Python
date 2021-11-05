#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Проверка на палиндром

def reverse_int(X):
    Y=0
    while X:
        Y=Y*10+X%10
        X=X//10
    return Y

def polyndrom(X):
    if X==reverse_int(X):
        return 1;
    return 0;

if 1==polyndrom(int(input("take me integer: "))):
    print("true")
else:
    print("false")
