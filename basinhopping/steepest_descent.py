import numpy as np
import itertools

class descent(object):
    def __init__(self, x, y, model, **kwargs):
        self.x = x
        self.y = y
        self.model = model

        self.iters = kwargs.pop('iters', 100)
        self.initial_parameters = kwargs.pop('initial_parameters', [1, 1])
        self.stepsize = kwargs.pop('stepsize', 0.5)

        self.best_params, self.path = self.fit()

    def fit(self):

        initial_fit = self.model(self.x, self.y, self.initial_parameters)

        f_old = np.sum((self.y - initial_fit)**2)
        f_new = 0
        best_params = self.initial_parameters
        count = 0
        path = []
        path.append(best_params)
        while f_new < f_old:
            if f_new != 0:
                f_old = f_new
            count +=1
            f = []
            tested_params = []
            for i in range(len(self.initial_parameters)):
                new_params = best_params.copy()
                new_params[i] = best_params.copy()[i] + self.stepsize
                fit = self.model(self.x, self.y, new_params)
                f.append(np.sum((self.y - fit)**2))
                tested_params.append(new_params)

            for i in range(len(new_params)):
                new_params = best_params.copy()
                new_params[i] = best_params.copy()[i] - self.stepsize
                fit = self.model(self.x, self.y, new_params)
                f.append(np.sum((self.y - fit)**2))
                tested_params.append(new_params)

            new_params = [best_params.copy()[i] + self.stepsize
                for i in range(len(best_params))]
            fit = self.model(self.x, self.y, new_params)
            f.append(np.sum((self.y - fit)**2))
            tested_params.append(new_params)

            new_params = [best_params.copy()[i] - self.stepsize
                for i in range(len(best_params))]
            fit = self.model(self.x, self.y, new_params)
            f.append(np.sum((self.y - fit)**2))
            tested_params.append(new_params)

            new_params = np.empty(len(best_params))
            for i in range(len(new_params)):
                if i%2:
                    new_params[i] = best_params.copy()[i] + self.stepsize
                if i%2 == 0:
                    new_params[i] = best_params.copy()[i] - self.stepsize
            fit = self.model(self.x, self.y, new_params)
            f.append(np.sum((self.y - fit)**2))
            tested_params.append(new_params)

            new_params = np.empty(len(best_params))
            for i in range(len(new_params)):
                if i%2:
                    new_params[i] = best_params.copy()[i] - self.stepsize
                if i%2 == 0:
                    new_params[i] = best_params.copy()[i] + self.stepsize
            fit = self.model(self.x, self.y, new_params)
            f.append(np.sum((self.y - fit)**2))
            tested_params.append(new_params)

            f_new = min(f)
            if f_new < f_old:
                for i in range(len(f)):
                    if f[i] == f_new:
                        best_params = tested_params[i]
                        path.append(best_params)
            if count == self.iters:
                print('Maximum iterations reached')
                break

        return best_params, path
