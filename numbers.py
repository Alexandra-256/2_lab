#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Enter four different numbers.")
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
d=int(input("Enter the fourth number: "))
s1=a+b
print("The sum of the first pair numbers is %s " % (s1))
s2=c+d
print("The sum of the second pair numbers is %s" % (s2))
x=s1/s2
print("Division of sums equals %.2f" % x)
