import numpy as np


def floyd(n, d, p):
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    p[i][j] = k + 1

    return d, p

n = int(input('Please enter numbers of nodes : '))
bignum = 999999999
w = np.empty((n, n),dtype=int)
d = w
p = np.zeros((n, n),dtype=int)
print("enter your numbers (instead of ∞ press $ and then enter)")

for numarrayI in range(1, n + 1):
    for numarrayJ in range(1, n + 1):
        print("enter [{}][{}] = ".format(numarrayI, numarrayJ))
        c = input()
        if c == '$':
            w[numarrayI - 1, numarrayJ - 1] = bignum
        else:
            w[numarrayI - 1, numarrayJ - 1] = int(c)


a, b = floyd(n, d, p)

print("the Least path for each node : \n")
print(a);
print("\n\n")
print("P matrix :\n")
print(b)
