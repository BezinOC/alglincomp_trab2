import numpy as np

class Function:
    def __init__(self, h, m, c, a1, a2, a3, w1, w2, w3):
        self.m = m
        self.c = c
        self.a = [a1, a2, a3]
        self.w = [w1, w2, w3]
        self.y0 = 0
        self.t0 = 0
        self.yl0 = 0
        self.yi = [self.y0]
        self.ti = [self.t0]
    
    def evaluate(self, t, y, yl):
        Ft = self.a[0] * np.sin(self.w[0] * t) + self.a[1] * np.sin(self.w[1] * t) + self.a[2] * np.cos(self.w[2] * t)
        k = (-self.m * yll_t - self.c * yl + Ft) / y
        return k

    def calculate(self, t, y, yl, k):
        h = 0.1
        K1 = 1/2 * h * self.evaluate(t, y, yl)
        Q = 1/2 * h * (yl + 1/2*K1)
        K2 = 1/2 * h * self.evaluate(t + h/2, y + Q, yl + K1)
        K3 = 1/2 * h * self.evaluate(t + h/2, y + Q, yl + K2)
        L = h * (yl + K3)
        K4 = 1/2 * h * self.evaluate(t + h, y + L, yl + 2*K3)
        next_y = y + (h)*(yl + 1/3*(K1 + K2 + K3))
        next_t = k * h
        next_yl = yl + 1/3 * (K1 + 2*K2 + 2*K3 + K4)
        return (next_y, next_t, next_yl)
    
    def runge_kutta(self):
        t = self.t0
        y = self.y0
        yl = self.yl0
        k = 1
        while k <= 10: # checar N (nesse caso está como 10)
            y_t_yl = self.calculate(t, y, yl, k)
            y = y_t_yl[0]
            t = y_t_yl[1]
            yl = y_t_yl[2]
            self.ti.append(t)
            self.yi.append(t)
            k += 1
    

f = Function(m=1, c=0.1, k=2, a1=1, a2=2, a3=1.5, w1=0.05, w2=1, w3=2)
