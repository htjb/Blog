import numpy as np
import matplotlib.pyplot as plt
from steepest_descent import descent, parameter_space

x = np.linspace(0, 10, 100)
y = 5*x + 5*x**2

def model(x, y, params):
    y_fit = params[0] * x + params[1] *x**2
    return y_fit

best_params = descent(x, y, model, initial_parameters=[4, 8]).best_params

plt.plot(x, y, label='"Data"')
plt.plot(x, model(x, y, best_params), label='Fit')
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.legend(fontsize=12)
plt.savefig('Initial_parameters[4,8].png')
plt.show()

parameter_space(x, y, model, initial_parameters=[4, 8])
