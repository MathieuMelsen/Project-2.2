# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 16:30:53 2025

@author: Mathieu en Merlijn
Geen gebruik gemaakt van chatgpt.

"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

# Gegevens
N = np.array([13, 24, 19, 21, 14])
l0 = 0.10  # m
l = 532e-9  # golflengte
DT = np.array([-4.5, -13.2, -10.7, -11.6, -5.3])


def fit(T, a, b):
    return a * (l0/(2*l)) * T + b


popt, pcov, infodict, mesg, ier = sp.optimize.curve_fit(
    fit, DT, N, [-0.12e-7, 0], full_output=True)
x = np.linspace(-4, -15, 1000)
plt.plot(x, fit(x, popt[0], popt[1]),color= 'darkturquoise')
plt.scatter(DT, N,color='coral')
plt.xlabel('Temperatuurverschil (K)')  
plt.ylabel('Aantal fringes') 
plt.show()
print(popt[0], popt[1])
