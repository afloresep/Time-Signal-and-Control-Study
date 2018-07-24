#!/usr/bin/python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

A= input("Please, introduce the amplitude of the signal  ")
T= input("Please, introduce the period  ")
f= input("Please, introduce the frequency ")
L= input("Please, introduce the lenght  ")

i= np.arange(T,L,T)
x= A*np.sin((2*np.pi*f)*i)
plt.plot(i,x)
plt.ylabel('x(t)')
plt.xlabel('t(s)')
plt.title('Known time signal ')
plt.show()

#creo que estoy operando mal, el resultado es parecido al de una sinusoide pero no es curva
