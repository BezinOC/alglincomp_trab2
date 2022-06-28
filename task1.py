import os
from config import config
settings = config.Settings()

class Function:

    def __init__(self, icod, tolm, t1, t2):
        self.tolm = tolm
        self.icod = icod
        self.t = [t1, t2]

    def evaluate_f1(self, x):
        x2, x3, x4 = x[0], x[1], x[2]
        x = 2*(x3**2) + (x2**2) + 6*(x4**4) - 1
        #x1, x2 = x[0], x[1]
        #x = x1 + 2*x2 - 2
        return x

    def evaluate_f2(self, x):
        x2, x3, x4 = x[0], x[1], x[2]
        x = 8*(x3**3) + 6*x3*(x2**2) + 36*x3*x2*x4 + 108*x3*(x4**2) - self.t[0]
        #x1, x2 = x[0], x[1]
        #x = x1**2 + 4*x2**2 - 4
        return x 

    def evaluate_f3(self, x):
        x2, x3, x4 = x[0], x[1], x[2]
        x = 60*(x3**4) + 60*(x3**2)*(x2**2) + 576*(x3**2)*x2*x4 + 2232*(x3**2)*(x4**2) + 252*(x4**2)*(x2**2) + 1296*(x4**3)*x2 + 3348*(x4**4) + 24*(x2**3)*x4 + 3*x2 - self.t[1]
        return x

    def evaluate_f(self, x):
        return [self.evaluate_f1(x), self.evaluate_f2(x), self.evaluate_f3(x)]

    def jacobian_evaluate(self, x):
        x2, x3, x4 = x[0], x[1], x[2]
        l1 = [2*x2, 4*x3, 12*x4]
        l2 = [120*x2*x3+36*x3*x4, 24*x3**2+60*x2*2+36*x2*x4+108*x4**2, 216*x3*x4+36*x2*x3]
        l3 = [1296*x4**3+504*x2*x4**2+576*x3**2*x4+72*x2**2*x4+120*x2*x3**2, 240*x3**3+120*x2**2*x3+1152*x2*x3*x4+4464*x3*x4**2+3, 13392*x4**2+3888*x2*x4**2+4464*x3**2*x4+504*x2**2*x4+576*x2*x3**2+24*x2**3]
        return [l1, l2, l3]
        # x1, x2 = x[0], x[1]
        # l1 = [1,2]
        # l2 = [2*x1,8*x2]
        # return [l1, l2]

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

    def mult_vector_matrix(self, a, b):
        tam_a, tam_b = len(a), len(b[0])
        m = []
        for i in range(tam_a):
            l = []
            for j in range(tam_b):
                l.append(a[i] * b[0][j])
            m.append(l)
        return m

    def mult_matrix(self, a, b):
        nlinhas_a, ncolunas_a = len(a), len(a[0])
        nlinhas_b, ncolunas_b = len(b), len(b[0])
        if ncolunas_a != nlinhas_b:
            print("Dimensoes erradas")
            return -1
        m = []
        for i in range(nlinhas_a):
            linha = []
            for j in range(ncolunas_b):
                soma = 0
                for k in range(ncolunas_a):
                    soma += a.loc[i][k] * b.loc[k][j]
                linha.append(soma)
            m.append(linha)
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
        
    def add(self, x, y):
        sum = []
        tam = len(x)
        if tam != len(y): raise Exception("Arrays must be same size")
        for i in range(tam): sum.append(x[i] + y[i])
        return sum

    def sub(self, x, y):
        sum = []
        tam = len(x)
        if tam != len(y): raise Exception("Arrays must be same size")
        for i in range(tam): sum.append(x[i] - y[i])
        return sum

    def t(self, m):
        mt = []
        rows, cols = len(m), len(m[0])
        for i in range(rows):
            l = []
            for j in range(cols):
                l.append(m[j][i])
            mt.append(l)
        return mt

    def newton_raphson(self):
        x = [1, 0, 0]
        niter = 10000
        for iter in range(1,niter):
            j = self.jacobian_evaluate(x)
            f = self.evaluate_f(x)
            delta_x =  self.mult_matrix_vector(self.inverse3(j), f)
            x = self.sub(x, delta_x)
            tol = self.norm(delta_x) / self.norm(x)
            if tol < self.tolm:
                print("Niter: {}".format(iter))
                return x
        raise Exception("Maximum number of interations reached")

    def inc_b(self, b, delta_x, y):
        for i in range(len(delta_x)): delta_x[i] *= -1
        bdx = self.mult_matrix_vector(b, delta_x)
        t_delta_x = [delta_x]
        inc = self.mult_vector_matrix(self.sub(y, bdx), t_delta_x)
        den = self.mult_matrix_vector(t_delta_x, delta_x)[0]
        for i in range(len(b)):
            for j in range(len(b[0])):
                    inc[i][j] /= den
        tam = len(b)
        for i in range(tam):
            for j in range(tam):
                b[i][j] += inc[i][j]
        return b

    def broyden(self):
        x = [1, 0, 0]
        b = self.jacobian_evaluate(x)
        niter = 10000
        for iter in range(1,niter):
            j = b
            f = self.evaluate_f(x)
            delta_x =  self.mult_matrix_vector(self.inverse3(j), f)
            x = self.sub(x, delta_x)
            y =  self.sub(self.evaluate_f(x), f)
            tol = self.norm(delta_x) / self.norm(x)
            if tol < self.tolm:
                print("Niter: {}".format(iter))
                return x
            else:
                b = self.inc_b(b, delta_x, y)       
        raise Exception("Maximum number of interations reached")

    def solve(self):
        t1, t2 = self.t[0], self.t[1]
        file_path = r"t1_" + str(t1) + r"_t2_" + str(t2) + r".txt"
        if self.icod == 1:
            x = self.newton_raphson()
        elif self.icod == 2:
            x = self.broyden()
        else:
            raise Exception("Icod must be 1 (Newton) or 2 (Broyden)")

        s = settings.task1[self.icod]
        path = os.path.join(s["out_path"], file_path)
        
        with open(path, 'w') as f:
            f.write("METODO ESCOLHIDO: " + s["name"] + "\n")
            f.write("TOL: " + str(self.tolm) + "\n")
            f.write("INPUTS: t1 = " + str(t1) + "; t2 = " + str(t2) + "\n")
            f.write("OUTPUTS: "  + "\n")
            for i in range(len(x)):
                f.write("c" + str(i+2) + " = " + str(x[i]) + "\n")
            f.close()

        print("SUCESSFULLY SOLVED")


if __name__ == "__main__":

    icod = 2
    t1 = 0.5
    t2 = 5
    tolm = 0.0001

    x = Function(icod=icod, t1=t1, t2=t2, tolm=tolm)
    print()
    x.solve()
    print()