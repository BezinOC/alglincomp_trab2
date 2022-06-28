import numpy as np

class Function:
    def __init__(self, h, T, m, c, k, a1, a2, a3, w1, w2, w3):
        self.h = h
        self.T = T
        self.m = m
        self.c = c
        self.k = k
        self.a = [a1, a2, a3]
        self.w = [w1, w2, w3]
        self.x0 = 0
        self.t0 = 0
        self.xl0 = 0
        self.N = T/h
        self.xi = [self.x0]
        self.ti = [self.t0]
    
    def evaluate(self, t, x, xl):
        Ft = self.a[0] * np.sin(self.w[0] * t) + self.a[1] * np.sin(self.w[1] * t) + self.a[2] * np.cos(self.w[2] * t)
        # F_t = self.m * 
        return None

    def calculate(self, t, x, xl, k):
        K1 = 1/2 * self.h * self.evaluate(t, x, xl)
        Q = 1/2 * self.h * (xl + 1/2*K1)
        K2 = 1/2 * self.h * self.evaluate(t + self.h/2, x + Q, xl + K1)
        K3 = 1/2 * self.h * self.evaluate(t + self.h/2, x + Q, xl + K2)
        L = self.h * (xl + K3)
        K4 = 1/2 * self.h * self.evaluate(t + self.h, x + L, xl + 2*K3)
        next_x = x + (self.h)*(xl + 1/3*(K1 + K2 + K3))
        next_t = k * self.h
        next_xl = xl + 1/3 * (K1 + 2*K2 + 2*K3 + K4)
        return (next_x, next_t, next_xl)
    
    def runge_kutta(self):
        t = self.t0
        x = self.x0
        xl = self.xl0
        k = 1
        while k <= self.N:
            x_t_xl = self.calculate(t, x, xl, k)
            x = x_t_xl[0]
            t = x_t_xl[1]
            xl = x_t_xl[2]
            self.ti.append(t)
            self.xi.append(t)
            k += 1
