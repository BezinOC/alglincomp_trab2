import math, os
from config import config
settings = config.Settings()

class Function:

    def __init__(self, icod, c1, c2, c3, c4, tolm=0.0001, icod2 = 1, a=1, b=2, n=3, x=3, dx=0.00001, dx2=0.00002):
        self.tolm = tolm
        self.icod = icod
        self.c = [c1, c2, c3, c4]
        self.icod2 = icod2
        self.a = a
        self.b = b
        self.n = n
        self.x = x
        self.dx = dx
        self.dx2 = dx2
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
            fa = self.evaluate(a)
            fb = self.evaluate(b)
            if f > 0:
                if fa > 0:
                    a = x
                else:
                    b = x
            else:
                if fa < 0:
                    a = x
                else: 
                    b = x
            if niter > 100: raise Exception("Maximum number of interations reached")
            niter += 1
        return x

    def newton_raphson(self, x=1):
        x0 = x
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
        wi = settings.wi_pol[n]
        sum = 0
        for i in range(1, n+1):
            sum += self.evaluate(a + delta*(i-1)) * l * wi[i]
        return sum

    def quadratura(self, a, b, n):
        if n < 2 or n > 10:
            raise Exception("N must be between 2 and 10")
        l = b - a
        wi = settings.wi_gauss[n]
        ti = settings.ti_gauss[n]
        sum = 0
        for i in range(1, n+1):
            sum += self.evaluate(a + ((l/2) * (ti[i]+1))) * wi[i]
        sum *= l/2
        return sum

    def solve(self):

        c1, c2, c3, c4 = self.c[0], self.c[1], self.c[2], self.c[3]
        file_path = r"c1_" + str(c1) + r"_c2_" + str(c2) + r"_c3_" + str(c3) + r"_c4_" + str(c4) + r".txt"

        if self.icod == 1:
            if self.icod2 == 1:
                x = self.newton_raphson()
            elif self.icod2 == 2:
                x = self.biss(self.a, self.b)
            else:
                raise Exception("Icod2 must be 1 or 2 for Icod == 1")
        elif self.icod == 2:
            if self.icod2 == 1:
                x = self.int_polinomial(self.a, self.b, self.n)
            elif self.icod2 == 2:
                x = self.quadratura(self.a, self.b, self.n)
            else:
                raise Exception("Icod2 must be 1 or 2 for Icod == 2")
        elif self.icod == 3:
            if self.icod2 == 1:
                x = self.foward_dif(self.x, self.dx)
            elif self.icod2 == 2:
                x = self.back_dif(self.x, self.dx)
            elif self.icod2 == 3:
                x = self.central_dif(self.x, self.dx)
            else:
                raise Exception("Icod2 must be 1, 2 or 3 for Icod == 3")
        elif self.icod == 4:
            if self.icod2 == 1:
                x = self.richard(self.x, self.dx, self.dx2)
            else:
                raise Exception("Icod2 must be 1 for Icod == 4")
        else:
            raise Exception("Icod must be equal to 1, 2, 3 or 4")

        s = settings.task2[self.icod][self.icod2]
        path = os.path.join(s["out_path"], file_path)

        with open(path, 'w') as f:
            f.write("METODO ESCOLHIDO: " + s["name"] + "\n")
            f.write("INPUTS: c1 = " + str(c1) + "; c2 = " + str(c2) + "; c3 = " + str(c3) + "; c4 = " + str(c4) + "\n")
            f.write("OUTPUT: x = "  +  str(x) +"\n")
            f.close()

        # print("SUCESSFULLY SOLVED")


if __name__ == "__main__":

    #icod = 1
    c1 = 0.25
    c2 = 1.2
    c3 = -3
    c4 = 1.2
    tolm = 0.0001
    #icod2 = 1
    a = 1
    b = 5
    n = 10
    x = 2
    dx = 0.1
    dx2 = 2

    icod = [1,2,3,4]
    icod2 = [[1,2], [1,2], [1,2,3], [1]]

    for i in icod:
        for j in icod2[i-1]:
            k = Function(icod=i, c1=c1, c2=c2, c3=c3, c4=c4, tolm=tolm, icod2=j, a=a, b=b, n=n, x=x, dx=dx, dx2=dx2)
            print()
            k.solve()
            print("OK")
            print()



