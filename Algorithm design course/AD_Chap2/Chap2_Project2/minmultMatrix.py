import numpy as np


def minmult(n, d, p):
    m = np.zeros((n + 1, n + 1), dtype=int)

    for i in range(1, n + 1):
        m[i][i] = 0
    for diagonal in range(1, n - 1 + 1):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal
            m[i, j] = m[i][i] + m[i + 1][j] + d[0][i - 1] * d[0][i] * d[0][j]
            p[i, j] = i
            for k in range(i + 1, j - 1 + 1):
                if m[i][k] + m[k + 1][j] + d[0][i - 1] * d[0][k] * d[0][j] < m[i][j]:
                    m[i][j] = m[i][k] + m[k + 1][j] + d[0][i - 1] * d[0][k] * d[0][j]
                    p[i][j] = k
    return m[1:, 1:], p[1:, 1:]


def order(i,j,Str_order):
    global Str
    if i == j:
        Str = Str + Str_order + f"A{i}"
    else:
        k = p[i][j]
        Str = Str + Str_order + "("
        order(i, k,Str_order)
        order(k + 1, j,Str_order)
        Str = Str + Str_order +")"



Str = ''
n = int(input("how many matrix you want to enter : "))

p = np.zeros((n, n+1),dtype=int)
d = np.empty((1,n+1),dtype=int)

print("plese enter your dimensions from d0 d1 .... dn")

for j in range (0,n+1):
    print("d{} = ".format(j))
    d[0,j] = int(input())




a , b = minmult(n,d,p)
print("d : ") ; print(d);print("\n")
print("M : ") ;print(a); print("\n")
print("P : "); print(b) ; print("\n")
print(f"order(1,{n}) : ")
order(1,n,Str)
print(Str)