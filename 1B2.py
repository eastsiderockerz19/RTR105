

'''
from math import sin
x = float(input("lietotaj, ludzu ievadi argumentu (x):"))
y = sin(x)
print("sin(%6.2f) = %6.2f"%(x,y))
k = 0
a = (-1)**0*x**2*0+1/(1)
S = a     
print("a0 = %6.2f S0 = %6.2f"%(a,S))

'''

from numpy import *
from matplotlib import pyplot as plt

x = linspace(0, 4, 70)
y = cos(x)

plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $cos(x)$')
plt.plot(x, y, color = '#FF0000', linewidth=5.0)

y1 = x
plt.plot(x, y1, color = '#00FF00', linewidth=5.0)

y2 = x - x*x*x/(1*2*3)
plt.plot(x, y2, color = '#0000FF', linewidth=5.0)

y3 = x - x*x*x/(1*2*3) + x*x*x*x*x/(1*2*3*4*5)
plt.plot(x, y3, color = '#3343FF', linewidth=5.0)

y4 = x - y2 - x*x*x*x*x*x*x/(1*2*3*4*5*6*7)
plt.plot(x, y4, color = '#FF3356', linewidth=5.0)

plt.show()



           
