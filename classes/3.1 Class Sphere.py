#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Написать класс Sphere для представления сферы в трехмерном пространстве
#
#   • конструктор, принимающий 4 действительных числа: радиус, и 3 координаты центра шара.
#   Если конструктор вызывается без аргументов, создать объект сферы с единичным радиусом и центром в начале координат.
#   • метод get_volume (), который возвращает действительное число — объем шара, ограниченной текущей сферой.
#   • метод get_square_(), который возвращает действительное число — площадь внешней поверхности сферы.
#   • метод get_radius_(), который возвращает действительное число — радиус сферы.
#   • метод get_center_(), который возвращает тьюпл с 3 действительными числами — координатами
#   центра сферы в том же порядке, в каком они задаются в конструкторе.
#   • метод set_center (x, y, z), который принимает 3 аргумента — действительных числа, 
#   и меняет координаты центра сферы, ничего не возвращая. Координаты задаются в том же порядке, что и в конструкторе.
#   • метод set_radius_(r), который принимает 1 аргумент — действительное число, и меняет радиус текущей сферы,
#   ничего не возвращая.
#   • метод is_point_inside (x, y, z), который принимает 3 аргумента — действительных числа — координаты 
#   некоторой точки в пространстве (в том же порядке, что и в конструкторе), и возвращает логическое
#   значение True или False в зависимости от того, находится эта точка внутри сферы.

import math

class Sphere:
    rad=0
    x=0
    y=0
    z=0
    
    def __init__(self,rad=1,x=0,y=0,z=0):
        self.rad=rad
        self.x=x
        self.y=y
        self.z=z 
    def get_volume(self):
        return (4/3)*math.pi*(self.rad**3)
    def get_square(self):
        return (self.rad**2)*math.pi*4
    def get_rad(self):
        return self.rad
    def get_center(self):
        return [self.x,self.y,self.z]
    def set_radius(self, rad):
        self.rad=rad
    def set_center(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z
# Для решения задачи, решено находить дистанцию между точками и сравнивать её с радиусом.
    def is_point_inside(self,x=0,y=0,z=0):
        mdist=[math.fabs(self.x-x),math.fabs(self.y-y),math.fabs(self.z-z)]
        dist=math.sqrt((mdist[2]**2)+(math.sqrt((mdist[1]**2)+(mdist[0]**2))**2))
        #print ('distance ',dist)
        return dist<=self.rad
        

def main():
    objSphere = Sphere(1, 1, 1, 1)
    objSphere.set_radius(3)
    objSphere.set_center(4,0,0)
    print ('Volume: ',objSphere.get_volume())
    print ('Square: ',objSphere.get_square())
    print ('Radius: ',objSphere.get_rad())
    print ('Center: ',objSphere.get_center())
    print ('inside: ',objSphere.is_point_inside())
    

if __name__=="__main__":
    main()

