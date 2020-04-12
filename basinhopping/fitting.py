import numpy as np
from basinhopping import hopping

x = np.linspace(0, 10, 100)
y = 5*x + 5*x**2

def model(x, y, params):
    y_fit = params[0] * x + params[1] *x**2
    return y_fit

best_params = hopping(x, y, model, initial_parameters=[4, 8],
    max_stepsize=10)
