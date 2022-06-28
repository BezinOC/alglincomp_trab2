import math
from config import config
settings = config.Settings()

class Function:

    def __init__(self, icod, c1, c2, c3, c4, tolm=0.0001, icod2 = 1):
        self.tolm = tolm
        self.icod = icod
        self.c = [c1, c2, c3, c4]
        self.icod2 = icod2
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
            if niter > 100: raise Exception("Maximum number of interations reached")
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
        raise Exception("Maximum number of interations reached")

    def int_polinomial(self, a, b, n):
        if n < 2 or n > 10:
            raise Exception("N must be between 2 and 10")
        l = b - a
        delta = l / (n - 1)
        wi = settings.wi[n]
        sum = 0
        for i in range(1, n+1):
            sum += self.evaluate(a + delta*(i-1)) * l * wi[i]
        return sum

    def solve(self):
        if self.icod == 1:
            if self.icod2 == 1:
                x = self.newton_raphson()
            elif self.icod2 == 2:
                x = self.biss()
            else:
                raise Exception("Icod2 must be 1 or 2 for Icod == 1")
        elif self.icod == 2:
            print(1)
        elif self.icod == 3:
            if self.icod2 == 1:
                x = self.foward_dif()
            elif self.icod2 == 2:
                x = self.back_dif()
            elif self.icod2 == 3:
                x = self.central_dif()
            else:
                raise Exception("Icod2 must be 1, 2 or 3 for Icod == 3")
        elif self.icod == 4:
            if self.icod2 == 1:
                x = self.richard()
            else:
                raise Exception("Icod2 must be 1 for Icod == 4")
        else:
            raise Exception("Icod must be equal to 1, 2, 3 or 4")

        # with open(path, 'w') as f:
        #     f.write("METODO ESCOLHIDO: " + s["name"] + "\n")
        #     f.write("INPUTS: t1 = " + str(t1) + "; t2 = " + str(t2) + "\n")
        #     f.write("OUTPUTS: "  + "\n")
        #     for i in range(len(x)):
        #         f.write("c" + str(i+2) + " = " + str(x[i]) + "\n")
        #     f.close()

        # print("SUCESSFULLY SOLVED")


if __name__ == "__main__":

    icod = 1
    c1 = -2
    c2 = 3
    c3 = 4
    c4 = -5
    tolm = 0.0001
    icod2 = 1

    x = Function(icod=icod, c1=c1, c2=c2, c3=c3, c4=c4, tolm=tolm, icod2=icod2)
    for i in range(2,11):
        print(x.int_polinomial(1,3,i))

# # print(f.foward_dif(x, d))
# # print(f.back_dif(x, d))
# # print(f.central_dif(x, d))
# # print(f.richard(x, dx1=d, dx2=d*2))

# print(f.newton_raphson())
# print(f.biss(-1, 1))
