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
        print(best_params)
        return best_params, path

class parameter_space(object):
    def __init__(self, x, y, model, **kwargs):
        self.x = x
        self.y = y
        self.model = model

        self.iters = kwargs.pop('iters', 100)
        self.initial_parameters = kwargs.pop('initial_parameters', [1, 1])
        self.stepsize = kwargs.pop('stepsize', 0.5)
        self.parameter_limits = kwargs.pop('parameter_limits',
            [[0, 10],[0, 10]])

        self.plot()

    def plot(self):

        def parameter_array(nums):
            return np.array(list(product(*((x, x) for x in nums))))

        p0 = np.arange(self.parameter_limits[0][0],
            self.parameter_limits[0][1] + self.stepsize, self.stepsize)

        p1 = np.arange(self.parameter_limits[1][0],
            self.parameter_limits[1][1] + self.stepsize, self.stepsize)

        combinations = list(itertools.product(p0,p1))
        f = []
        for i in range(len(combinations)):
            f.append(np.sum((self.y -self.model(self.x, self.y,
                combinations[i]))**2))
        f = np.array(f)

        import matplotlib.pyplot as plt
        import matplotlib.colors as colors
        import matplotlib.cm as cmx

        path = descent(self.x, self.y, self.model,
            stepsize=self.stepsize,
            initial_parameters=self.initial_parameters).path
        path_x, path_y = [], []
        for i in range(len(path)):
            path_x.append(path[i][0])
            path_y.append(path[i][1])

        fig, ax = plt.subplots()
        jet = plt.get_cmap('jet')
        cNorm = colors.Normalize(vmin=0,vmax=1)
        scalarMap = cmx.ScalarMappable(norm=cNorm,cmap=jet)
        dummy_cax = ax.scatter(f/f.max(),f/f.max(),c=f/f.max(),cmap=jet)
        ax.cla()
        for i in range(len(f)):
            colourVal=scalarMap.to_rgba(f[i]/f.max())
            ax.plot(combinations[i][0], combinations[i][1],
                c=colourVal, marker='s', markersize=30*self.stepsize, zorder=2)
        fig.colorbar(dummy_cax, label=r'$f/f_{max}$')
        plt.plot(path_x, path_y, c='k')
        plt.plot(path_x[-1], path_y[-1], c='k', marker='*')
        plt.xlabel(r'$P_0$', fontsize=12)
        plt.ylabel(r'$P_1$', fontsize=12)
        plt.show()
        plt.close()
