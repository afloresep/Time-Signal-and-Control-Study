#!/usr/bin/python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

A= input("Please, introduce the amplitude of the signal  ")
T= input("Please, introduce the period  ")
f= input("Please, introduce the frequency ")
L= input("Please, introduce the lenght  ")
i= np.arange(T,L,T)
Signal= A*np.sin((2*np.pi*f)*i)


resultados:
  -7.64253880e-14  -1.52850776e-13  -2.29276164e-13  -3.05701552e-13
  -3.82126940e-13  -4.58552328e-13  -5.34977716e-13  -6.11403104e-13
   6.76413560e-13  -7.64253880e-13   5.23562784e-13  -9.17104656e-13
   3.70712008e-13  -1.06995543e-12   2.17861232e-13  -1.22280621e-12
   6.50104561e-14   1.35282712e-12   2.64064379e-12  -1.52850776e-12
  -2.40691096e-13   1.04712557e-12   2.33494223e-12  -1.83420931e-12
  -5.46392648e-13   7.41424016e-13   2.02924068e-12  -2.13991086e-12
  -8.52094200e-13   4.35722464e-13   1.72353913e-12  -2.44561242e-12
  -1.15779575e-12]
