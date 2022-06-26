
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
        self.N = T/h
        self.xi = [self.x0]
        self.ti = [self.t0]
    
    def evaluate(self, t, x):
        return None

    def calculate(self, t, x):
        K1 = self.evaluate(t, x)
        K2 = self.evaluate(t + self.h/2, x + (self.h/2)*K1)
        K3 = self.evaluate(t + self.h/2, x + (self.h/2)*K2)
        K4 = self.evaluate(t + self.h, x + self.h*K3)
        next_x = x + (self.h/6)*(K1 + 2*K2 + 2*K3 + K4)
        return next_x
