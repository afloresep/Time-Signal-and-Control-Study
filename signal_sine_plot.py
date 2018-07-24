#!/usr/bin/python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
A= input("Please, introduce the amplitude of the signal  ")
T= input("Please, introduce the period  ")
L= input("Please, introduce the lenght  ")
i= np.arange(T,L,T)
x= A*np.sin((2*np.pi)/i)
print x
plt.plot(i,x)
plt.title('TIME KNOWN SIGNAL')
plt.ylabel("x(t)")
plt.xlabel("time(s)")
plt.show()
