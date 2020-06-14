import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def fitting(x, a, b):
    y_fit = a*x**2 + b*x
    return y_fit

x = np.arange(-10, 20, 1)
y = 1.4*x**2 + 0.2*x + 4.3*x**3

p0 = [1, 1]
parameters, cov = curve_fit(fitting, x, y, p0=p0)
print(parameters)

param1 = np.linspace(parameters[0]*0.5, parameters[0]*1.5, 100)
param2 = np.linspace(parameters[1]*0.5, parameters[1]*1.5, 100)

X, Y = np.meshgrid(param1, param2)

Z = np.empty(X.shape)
for i in range(len(X)):
    for j in range(X.shape[0]):
        Z[i, j] = (np.sum((y - fitting(x, X[i,j], Y[i,j]))**2))

fig = plt.figure()

cp = plt.contourf(X, Y, Z, cmap='jet')
plt.colorbar(cp, label=r'$\chi^2$')

plt.xlabel(r'$a$')
plt.ylabel(r'$b$')
plt.savefig('chi2_example.png')
plt.show()
