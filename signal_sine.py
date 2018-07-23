#!/usr/bin/python
# coding=utf-8
import numpy as np
A= input("Please, introduce the amplitude of the signal  ")
T= input("Please, introduce the period  ")
L= input("Please, introduce the lenght  ")
i= np.arange(0,L,T)
xt= A*np.sin((2*np.pi)/x)
print xt
# el resultado para T= 1.5, A= 3.0 , L= 50 es el siguiente:
--2.59807621  2.59807621  2.95442326  2.59807621  2.22943448
  1.92836283  1.68996017  1.5         1.34639754  1.22020993  1.11498737
  1.02606043  0.95000398  0.88426552  0.82691207  0.77645714  0.73174116
  0.69184761  0.65604327  0.62373507  0.59443843  0.56775373  0.54334863
  0.52094453  0.50030624  0.48123384  0.46355638  0.4471268   0.43181794
  0.4175193   0.40413439  0.39157858  0.37977736
