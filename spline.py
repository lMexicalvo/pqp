#! /usr/bin/python3
# -*- coding: utf-8 -*-
#
#_________________________________________________________
# Universidade Federal de Santa Catarina
# Departamento de Engenharias da Mobilidade
# Curso de Cálculo Numérico
# Prof. Alexandre Zabot
# https://zabot.paginas.ufsc.br
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
import sys
import matplotlib.pyplot as plt
import numpy as np
import interpolacao

ifile = sys.argv[1]
X, Y = np.loadtxt( ifile, unpack=True, dtype=float )

coef = interpolacao.solve_spline( X, Y, derivatives=[], verbose=True )

nn = 100*len(X)
xx = np.linspace(X[0],X[-1],nn)
yy = interpolacao.calc_spline( X, xx, coef )


plt.plot( X , Y , "o" )
plt.plot( xx, yy, "-" )
plt.grid()
plt.margins(0.1)
plt.show()
