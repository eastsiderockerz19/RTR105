from numpy import *
x = linspace(0, 7, 70)
y = cos(x)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $cos(x)$')
plt.plot(x, y, color = '#FF0000')
plt.show()


from numpy import *
x = linspace(0, 7, 70)
y2 = sin(x)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $sin(x)$')
plt.plot(x, y2, color = '#33FF6B')
plt.show()
