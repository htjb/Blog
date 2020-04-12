import numpy as np
from steepest_descent import descent

class hopping(object):
    def __init__(self,x, y, model, **kwargs):
        self.x = x
        self.y = y
        self.model = model

        self.iters = kwargs.pop('iters', 1000)
        self.descent_iters = kwargs.pop('descent_iters', 1000)
        self.initial_parameters = kwargs.pop('initial_parameters', [1, 1])
        self.stepsize = kwargs.pop('stepsize', 0.5)
        self.maxstepsize = kwargs.pop('max_stepsize', 5)
        self.success_iters = kwargs.pop('success_iters', 50)
        self.interval = kwargs.pop('interval', 10)

        self.best_params = self.fit()

    def fit(self):

        res = descent(self.x, self.y, self.model,
            initial_parameters=self.initial_parameters,
            stepsize=self.stepsize, iters=self.descent_iters)
        best_params = res.best_params
        f_best = np.sum((self.y - self.model(self.x, self.y, best_params))**2)

        count = 0
        count_change = 0
        while count <= self.iters:
            if count == 0:
                step = self.maxstepsize
            if count%self.interval == 0 and count != 0:
                step /= 2
            r = np.random.randint(0, 2, len(self.initial_parameters))
            initial_params = np.empty(len(best_params))
            for i in range(len(r)):
                initial_params[i] = best_params[i] + \
                        (-1)**r[i]*np.random.uniform(0, step, 1)
            res = descent(self.x, self.y, self.model,
                initial_parameters=initial_params,
                stepsize=self.stepsize, iters=self.descent_iters)
            params = res.best_params
            f = np.sum((self.y - self.model(self.x, self.y, params))**2)
            if f < f_best:
                if np.isclose(f, f_best, rtol=1e-5, atol=1e-5):
                    f_best = f
                    best_params = params
                    break
                f_best = f
                best_params = params
                count_change = 0
            else:
                count_change += 1
                if count_change == self.success_iters:
                    break
            print(count_change, f_best, f, params)
            count += 1

        return best_params
