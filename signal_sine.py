#!/usr/bin/python
# coding=utf-8
import sys
import math
A= int(input("Please, introduce the amplitude of the signal "))
T= int(input("Please, introduce the period (seconds)"))
w= (2*math.pi)/float(T)
L= int(input("Please, introduce the lenght: "))
for x in range(T,L):
    z= A*math.sin((2*math.pi)/x)
    print float(z)
