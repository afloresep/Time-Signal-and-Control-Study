
!/usr/bin/python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

A= input("Please, introduce the amplitude of the signal  ")
T= input("Please, introduce the period  ")
f= input("Please, introduce the frequency ")
L= input("Please, introduce the lenght  ")
i= np.arange(T,L,(T/100))
Signal= A*np.sin(2*np.pi*i/(T))
