import math
from msilib.schema import Error
import numpy as np

class Function:

    def __init__(self, icod, tolm, t1, t2):
        self.tolm = tolm
        self.icod = icod
        self.t = [t1, t2]

    def evaluate_f1(self, x):
        x2, x3, x4 = x[0], x[1], x[2]
        x = 2*(x3**2) + (x2**2) + 6*(x4**4) - 1
        return x

    def evaluate_f2(self, x):
        x2, x3, x4 = x[0], x[1], x[2]
        x = 8*(x3**3) + 6*x3*(x2**2) + 36*x3*x2*x4 + 108*x3*(x4**2) - self.t[0]
        return x 

    def evaluate_f3(self, x):
        x2, x3, x4 = x[0], x[1], x[2]
        x = 60*(x3**4) + 60*(x3**2)*(x2**2) + 576*(x3**2)*x2*x4 + 2232*(x3**2)*(x4**2) + 252*(x4**2)*(x2**2) + 1296*(x4**3)*x2 + 3348*(x4**4) + 24*(x2**3)*x4 + 3*x2 - self.t[1]
        return x

    def evaluate_f(self, x):
        return [self.evaluate_f1(x), self.evaluate_f2(x), self.evaluate_f3(x)]

    def jacobian_evaluate(self, x): #consertar essa merda depois
        x2, x3, x4 = x[0], x[1], x[2]
        # l1 = [2*x2, 4*x3, 24*(x4**3)]
        # l2 = [12*x3*(x2+3*x4), 6*((x2**2) + 6*x2*x4 + 4*(x3**2) + 18*(x4**2)), 36*x3*(x2+6*x4)]
        # l3 = [72*(x2**2)*x4 + 120*x2*(x3**2) + 504*x2*(x4**2) + 576*(x3**2)*x4 + 1296*(x4**3) + 3, 24*x3*(5*(x2**2) + 48*x2*x4 + 10*(x3**2) + 186*(x4**2)), 24*((x2**3) + 21*(x2**2)*x4 + 24*x2*(x3**2) + 162*x2*(x4**2) + 186*(x3**2)*x4) + 558*(x4**3)]
        # return [l1, l2, l3]
        l1 = [2*x2, 4*x3, 12*x4]
        l2 = [120*x2*x3+36*x3*x4, 24*x3**2+60*x2*2+36*x2*x4+108*x4**2, 216*x3*x4+36*x2*x3]
        l3 = [1296*x4**3+504*x2*x4**2+576*x3**2*x4+72*x2**2*x4+120*x2*x3**2, 240*x3**3+120*x2**2*x3+1152*x2*x3*x4+4464*x3*x4**2+3, 13392*x4**2+3888*x2*x4**2+4464*x3**2*x4+504*x2**2*x4+576*x2*x3**2+24*x2**3]
        return [l1, l2, l3]

    def mult_matrix_vector(self, a, b):
        nlinhas_a, ncolunas_a = len(a), len(a[0])
        nlinhas_b, ncolunas_b = len(b), 1
        if ncolunas_a != nlinhas_b:
            print("Dimensoes erradas")
            return -1
        m = []
        for i in range(nlinhas_a):
            soma = 0
            for j in range(ncolunas_a):
                soma += a[i][j] * b[j]
            m.append(soma)
        return m

    def det2(self, m):
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]

    def det3(self, m):
        return ((m[0][0]*m[1][1]*m[2][2] + m[0][1]*m[1][2]*m[2][0] + m[0][2]*m[1][0]*m[2][1]) 
        - (m[0][2]*m[1][1]*m[2][0] + m[0][0]*m[1][2]*m[2][1] + m[0][1]*m[1][0]*m[2][2]))

    def inverse2(self, m):
        det = self.det2(m)
        m_adj = [[m[1][1], -m[0][1]], [-m[1][0], m[0][0]]]
        for i in range(2):
            for j in range(2):
                m_adj[i][j] /= det
        return m_adj

    def inverse3(self, m):
        m_adj = [
            [self.det2([[m[1][1], m[1][2]], [m[2][1], m[2][2]]]), -self.det2([[m[1][0], m[1][2]], [m[2][0], m[2][2]]]), self.det2([[m[1][0], m[1][1]], [m[2][0], m[2][1]]])],
            [-self.det2([[m[0][1], m[0][2]], [m[2][1], m[2][2]]]), self.det2([[m[0][0], m[0][2]], [m[2][0], m[2][2]]]), -self.det2([[m[0][0], m[0][1]], [m[2][0], m[2][1]]])],
            [self.det2([[m[0][1], m[0][2]], [m[1][1], m[1][2]]]), -self.det2([[m[0][0], m[0][2]], [m[1][0], m[1][2]]]), self.det2([[m[0][0], m[0][1]], [m[1][0], m[1][1]]])]       
        ]
        det = self.det3(m)
        for i in range(3):
            for j in range(3):
                m_adj[i][j] /= det
        return m_adj

    def norm(self, x):
        norm = 0
        for i in x:
            norm += i**2
        norm = norm**(1/2)
        return norm

    def newton_raphson(self):
        x = [1,0,0]
        niter = 1000
        for iter in range(1,niter):
            j = self.jacobian_evaluate(x)
            f = self.evaluate_f(x)
            delta_x =  self.mult_matrix_vector(self.inverse3(j), f)
            for i in range(3): x[i] = x[i] - delta_x[i]
            tol = self.norm(delta_x) / self.norm(x)
            if tol < self.tolm:
                print("Niter: {}".format(iter))
                return x
        raise Exception("Maximum number of interations reached")

x = Function(icod=1, tolm=0.00001, t1=0.0, t2=11.667)
print(x.newton_raphson())