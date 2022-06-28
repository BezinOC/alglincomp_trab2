import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from config import config
settings = config.Settings()

class Function:
    def __init__(self, h, T, m, c, k, a1, a2, a3, w1, w2, w3):
        self.h = h
        self.T = T
        self.N = T/h
        self.m = m
        self.c = c
        self.k = k
        self.a = [a1, a2, a3]
        self.w = [w1, w2, w3]
        self.y0 = 0
        self.t0 = 0
        self.yl0 = 0
        self.yll0 = 0
        self.y = [self.y0]
        self.yl = [self.yl0]
        self.yll = [self.yll0]
    
    def evaluate(self, t, y, yl):
        Ft = self.a[0] * np.sin(self.w[0] * t) + self.a[1] * np.sin(self.w[1] * t) + self.a[2] * np.cos(self.w[2] * t)
        yll = (-self.c * yl - self.k * y + Ft) / self.m 
        return yll

    def calculate(self, t, y, yl, k):
        K1 = 1/2 * self.h * self.evaluate(t, y, yl)
        Q = 1/2 * self.h * (yl + 1/2*K1)
        K2 = 1/2 * self.h * self.evaluate(t + self.h/2, y + Q, yl + K1)
        K3 = 1/2 * self.h * self.evaluate(t + self.h/2, y + Q, yl + K2)
        L = self.h * (yl + K3)
        K4 = 1/2 * self.h * self.evaluate(t + self.h, y + L, yl + 2*K3)
        next_y = y + (self.h)*(yl + 1/3*(K1 + K2 + K3))
        next_t = k * self.h
        next_yl = yl + 1/3 * (K1 + 2*K2 + 2*K3 + K4)
        next_yll = self.evaluate(t, y, yl)
        return (next_y, next_t, next_yl, next_yll)
    
    def runge_kutta_nystrom(self):
        t = self.t0
        y = self.y0
        yl = self.yl0
        yll = self.yll0
        k = 1
        while k <= self.N:
            y_t_yl_yll = self.calculate(t, y, yl, k)
            y = y_t_yl_yll[0]
            t = y_t_yl_yll[1]
            yl = y_t_yl_yll[2]
            yll = y_t_yl_yll[3]
            self.y.append(y)
            self.yl.append(yl)
            self.yll.append(yll)
            k += 1
        table = pd.DataFrame(data={'deslocamento': self.y, 'velocidade': self.yl, 'aceleracao': self.yll, 'tempo': list(np.linspace(self.t0, self.T, int(self.N)+1))})

        s = settings.task3
        file_path = rf"m={str(self.m)}_c={str(self.c)}_k={str(self.k)}_a=" + r",".join(str(a) for a in self.a) + r"_w=" + ",".join(str(w) for w in self.w) + rf"_h={str(self.h)}_T={str(self.T)}.txt"
        file_path2 = rf"m={str(self.m)}_c={str(self.c)}_k={str(self.k)}_a=" + r",".join(str(a) for a in self.a) + r"_w=" + ",".join(str(w) for w in self.w) + rf"_h={str(self.h)}_T={str(self.T)}.xlsx"
        path = os.path.join(s["out_path"], file_path)
        path2 = os.path.join(s["out_path"], file_path2)
        np.savetxt(path, table)
        with open(path, 'a') as f:
            f.write("INPUTS: " + f"m={str(self.m)}_c={str(self.c)}_k={str(self.k)}_a=" + ", ".join(str(a) for a in self.a) + "_w=" + ", ".join(str(w) for w in self.w) + f"_h={str(self.h)}_T={str(self.T)}")
        table.to_excel(path2)
        table.plot(x='tempo', y='deslocamento', kind='line')
        plt.show()
        table.plot(x='tempo', y='velocidade', kind='line')
        plt.show
        print("SUCESSFULLY SOLVED")

if __name__ == "__main__":

    h=0.1 
    T=100
    m=1 
    c=0.1
    k=1
    a1=-1
    a2=2
    a3=1.5
    w1=0.2
    w2=1
    w3=2

    f = Function(h=h, T=T, m=m, c=c, k=k, a1=a1, a2=a2, a3=a3, w1=w1, w2=w2, w3=w3)


f.runge_kutta_nystrom()
