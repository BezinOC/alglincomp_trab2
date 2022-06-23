import math
from re import X

class Function:

    def __init__(self, icod, tolm, t1, t2):
        self.tolm = tolm
        self.icod = icod
        self.t = [t1, t2]

    def evaluate_f1(self, x2, x3, x4):
        x = 2*(x3**2) + (x2**2) + 6*(x4**4)
        return x

    def evaluate_f2(self, x2, x3, x4):
        x = 8*(x3**3) + 6*x3*(x2**2) + 36*x3*x2*x4 + 108*x3*(x4**2)
        return x 

    def evaluate_f3(self, x2, x3, x4):
        x = 60*(x3**4) + 60*(x3**2)*(x2**2) + 576*(x3**2)*x2*x4 + 2232*(x3**2)*(x4**2) + 252*(x4**2)*(x2**2) + 1296*(x4**3)*x2 + 3348*(x4**4) + 24*(x2**3)*x4 + 3*x2
        return x

    def jacobian_evaluate(self, x2, x3, x4):
        l1 = [2*x2, 4*x3, 24*(x4**3)]
        l2 = [12*x3*(x2+3*x4), 6*((x2**2) + 6*x2*x4 + 4*(x3**2) + 18*(x4**2)), 36*x3*(x2+6*x4)]
        l3 = [72*(x2**2)*x4 + 120*x2*(x3**2) + 504*x2*(x4**2) + 576*(x3**2)*x4 + 1296*(x4**3) + 3, 24*x3*(5*(x2**2) + 48*x2*x4 + 10*(x3**2) + 186*(x4**2)), 24*((x2**3) + 21*(x2**2)*x4 + 24*x2*(x3**2) + 162*x2*(x4**2) + 186*(x3**2)*x4) + 558*(x4**3)]
        return 1