import numpy as np
from steepest_descent import descent
import itertools

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
        self.parameter_limits = [[-10, 20], [-10, 20]]

        self.best_params = self.fit()

    def fit(self):

        def parameter_array(nums):
            return np.array(list(product(*((x, x) for x in nums))))

        p0 = np.arange(self.parameter_limits[0][0],
            self.parameter_limits[0][1] + self.stepsize, self.stepsize)

        p1 = np.arange(self.parameter_limits[1][0],
            self.parameter_limits[1][1] + self.stepsize, self.stepsize)

        combinations = list(itertools.product(p0,p1))
        try:
            f_array = np.loadtxt('gif/f_space.txt')
        except:
            print('here')
            f_array = []
            for i in range(len(combinations)):
                f_array.append(np.sum((self.y -self.model(self.x, self.y,
                    combinations[i]))**2))
            f_array = np.array(f_array)
            np.savetxt('gif/f_space.txt', f_array)

        import matplotlib.pyplot as plt
        import matplotlib.colors as colors
        import matplotlib.cm as cmx

        res = descent(self.x, self.y, self.model,
            initial_parameters=self.initial_parameters,
            stepsize=self.stepsize, iters=self.descent_iters)
        best_params = res.best_params
        print(best_params)
        f_best = np.sum((self.y - self.model(self.x, self.y, best_params))**2)
        print(f_best)

        count = 0
        count_change = 0
        fs = []
        f_bests = []
        while count <= self.iters:
            fig, ax = plt.subplots()
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

            jet = plt.get_cmap('jet')
            cNorm = colors.Normalize(vmin=0,vmax=1)
            scalarMap = cmx.ScalarMappable(norm=cNorm,cmap=jet)
            dummy_cax = ax.scatter(f_array/f_array.max(),f_array/f_array.max(),
                c=f_array/f_array.max(),cmap=jet)
            ax.cla()
            for i in range(len(f_array)):
                colourVal=scalarMap.to_rgba(f_array[i]/f_array.max())
                ax.plot(combinations[i][0], combinations[i][1],
                    c=colourVal, marker='s', markersize=30*self.stepsize)
            fig.colorbar(dummy_cax, label=r'$f/f_{max}$')
            plt.plot(initial_params[0], initial_params[1], marker='^', c='w',
                label='Initial_parameters', markeredgecolor='k')
            plt.plot(params[0], params[1], marker='o', c='w',
                label='Local Minimum', markeredgecolor='k')
            plt.plot(best_params[0], best_params[1], marker='*', c='w',
                label='Current Global Minimum', markeredgecolor='k')

            x1 = np.linspace(best_params[0]-step,
                best_params[0]+step, 100)
            y1 = [best_params[1]-step]*100
            x2 = np.linspace(best_params[0]-step,
                best_params[0]+step, 100)
            y2 = [best_params[1]+step]*100
            y3 = np.linspace(best_params[1]-step,
                best_params[1]+step, 100)
            x3 = [best_params[0]-step]*100
            y4 = np.linspace(best_params[1]-step,
                best_params[1]+step, 100)
            x4 = [best_params[0]+step]*100

            plt.plot(x1, y1, ls='--', c='k', label='Maximum Parameter Perturbation')
            plt.plot(x2, y2, ls='--', c='k')
            plt.plot(x3, y3, ls='--', c='k')
            plt.plot(x4, y4, ls='--', c='k')

            plt.xlabel(r'$P_0$', fontsize=12)
            plt.ylabel(r'$P_1$', fontsize=12)
            plt.xlim([-10, 20])
            plt.ylim([-10, 20])
            plt.legend(loc=3, fontsize='small')
            plt.savefig('gif/' + str(count) + '.png')
            plt.close()

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
            fs.append(f)
            f_bests.append(f_best)
            print(count_change, f_best, f, params)
            count += 1

        plt.figure()
        plt.plot(fs, label='Objective Evaluations')
        plt.plot(f_bests, label='Best Objective Evaluations')
        plt.xlabel('Iteration', fontsize=12)
        plt.ylabel(r'$X^2$', fontsize=12)
        plt.legend(fontsize=12)
        plt.yscale('log')
        plt.savefig('History.png')
        plt.show()
