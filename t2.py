import math

class Function:

    def __init__(self, icod, tolm, c1, c2, c3, c4):
        self.tolm = tolm
        self.icod = icod
        self.c = [c1, c2, c3, c4]
        #function = c1*exp(c2*x) + c3*x^c4

    def evaluate(self, x):
        x = self.c[0]*math.exp(self.c[1]*x) + self.c[2]*(x**(self.c[3]))
        return x

    def foward_dif(self, x, dx=0.00001):
        f_delta = self.evaluate(x + dx)
        f = self.evaluate(x)
        return (f_delta - f) / dx
    
    def back_dif(self, x, dx=0.00001):
        f = self.evaluate(x)
        f_delta = self.evaluate(x - dx)
        return (f - f_delta) / dx

    def central_dif(self, x, dx=0.00001):
        f_foward = self.evaluate(x + dx)
        f_back = self.evaluate(x - dx)
        return (f_foward - f_back) / (2*dx)

    def richard(self, x, dx1=0.00001, dx2=0.00001):
        d1 = self.foward_dif(x, dx1)
        d2 = self.back_dif(x, dx2)
        q_inv = dx2/dx1
        return d1 + ((d1-d2) / (q_inv - 1))

    def biss(self, a, b):
        if a > b: a,b = b,a
        x = (a+b)/2
        niter = 0
        while abs(a-b) > self.tolm:
            x = (a+b)/2
            f = self.evaluate(x)
            if f > 0:
                b = x
            else: 
                a = x
            if niter > 100: raise Exception("Número de iterações máximo excedido")
            niter += 1
        return x

    def newton_raphson(self, x0=1):
        niter = 0
        while (niter < 100):
            x1 = x0 - (self.evaluate(x0) / (self.central_dif(x0)))
            tol = abs(x1 - x0)
            if tol < self.tolm:
                return x1
            x0 = x1
        raise Exception("Número de iterações máximo excedido")

f = Function(icod=1, tolm=0.00001, c1=2, c2=3, c3=4, c4=5)
d = 0.00001
x = 1

# print(f.foward_dif(x, d))
# print(f.back_dif(x, d))
# print(f.central_dif(x, d))
# print(f.richard(x, dx1=d, dx2=d*2))

print(f.newton_raphson())
print(f.biss(-1, 1))
