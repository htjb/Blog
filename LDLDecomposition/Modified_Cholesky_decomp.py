import numpy as np

class decomp(object):
    def __init__(self, Q, **kwargs):
        self.Q = Q

        self.LDL = kwargs.pop('LDL', False)

        if self.LDL is False:
            self.L = self.cd()
        if self.LDL is True:
            self.L, self.D = self.cd()

    def cd(self):
        L = np.zeros(self.Q.shape)
        for i in range(L.shape[0]):
            for j in range(L.shape[1]):
                    if i == j:
                        L[i, j] = np.sqrt(self.Q[i, j] -
                            np.sum([pow(L[j, k], 2) for k in range(j)]))
                    elif i > j:
                        L[i, j] = (1/L[j, j])*(self.Q[i, j] -
                            np.sum([L[i, k]*L[j, k] for k in range(j)]))
        if self.LDL is False:
            return L
        if self.LDL is True:
            S = np.diag(L)
            D = S**2*np.identity(len(S))
            invS = 1/S
            L = L @ (invS * np.identity(len(S)))
            return L, D
