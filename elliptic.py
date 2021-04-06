#!/usr/bin/python3

import numpy as np

import matplotlib.pyplot as plt

import sys

a = -3
b = 5
file1 ='1111'

print ("y^2 - x^3 + 3*x - 5 = 0")
y, x = np.ogrid[-5:5:100j, -5:5:100j]
plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0])
plt.grid()
plt.savefig(file1)
plt.show()
print ("Saving to ",file1)

