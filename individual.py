#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Даны основания равнобедренной трапеции и угол при большем основании. Найти площадь трапеции.


import math

a = float(input("Введите длину большего основания: "))
b = float(input("Введите длину меньшего основания: "))
alpha = float(input("Введите угол при большем основании: "))
y = math.radians(alpha)
print("Площадь трапеции равна: ",(a**2-b**2)/4*y)



