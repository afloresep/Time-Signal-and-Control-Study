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
# el resultado para T= 1.5, A= 3.0 , L= 50 es el siguiente:
-7.34788079488e-16
3.67394039744e-16
2.59807621135
3.0
2.85316954889
2.59807621135
2.3454944474
2.12132034356
1.92836282906
1.76335575688
1.62192245237
1.5
1.39416951613
1.30165121735
1.22020992923
1.1480502971
1.08372499856
1.02606042998
0.974098407614
0.927050983125
0.884265523233
0.845197670524
0.809390313471
0.776457135308
0.746069661495
0.717946992863
0.691847612227
0.667562801869
0.644911320633
0.623735072453
0.603895560266
0.585270966048
0.567753733081
0.55124855345
0.535670684396
0.520944533001
0.507002460966
0.493783770842
0.481233842573
0.469303395121
0.457947852657
0.447126798529
0.436803503205
0.42694451482
0.41751930288
0.408499947289
0.399860866121
0.39157857666
0.383631485054
