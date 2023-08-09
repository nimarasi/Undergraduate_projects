import numpy as np


class spars():
    def __init__(self, i=0, j=0):
        self.array_ = np.zeros((i, j), dtype=int)

    def set_num(self, i, j, name):
        self.array_ = np.zeros((i, j), dtype=int)
        n = 0
        for ii in range(i):
            print("****next line****")
            for jj in range(j):
                print(f"please enter for {name}[{ii}][{jj}] number")
                n = int(input(f"[{ii}][{jj}] :"))
                self.array_[ii][jj] = n

    def is_spars(self, i, j):
        k = 0
        for ii in range(i):
            for jj in range(j):
                if self.array_[ii][jj] != 0:
                    k += 1
        if i * j / 3 > k:
            return True, k
        else:
            return False, 0

    def change(self, i, j, k):
        m = np.zeros((k, 3), dtype=int)
        satrm = 0
        sotonm = 0
        for ii in range(i):
            for jj in range(j):
                if self.array_[ii][jj] != 0:
                    m[satrm][sotonm] = ii
                    m[satrm][sotonm + 1] = jj
                    m[satrm][sotonm + 2] = self.array_[ii][jj]
                    satrm += 1
        return m

    def reverse(self, m, i, j, h):
        self.array_ = np.zeros((i, j), dtype=int)
        for ii in range(h):
            for jj in range(1):
                row = m[ii][jj]
                column = m[ii][jj + 1]
                self.array_[row][column] = m[ii][jj + 2]
        return self.array_

    def add(self, other, ka, kb):
        dicchangea = {}
        dicchangeb = {}
        dicadd = {}
        for ia in range(ka):
            for ja in range(1):
                dicchangea[str(self.array_[ia][ja]) + str(self.array_[ia][ja + 1])] = self.array_[ia][ja + 2]
        for ib in range(kb):
            for jb in range(1):
                dicchangeb[str(other.array_[ib][jb]) + str(other.array_[ib][jb + 1])] = other.array_[ib][jb + 2]
        for keya, valuea in dicchangea.items():
            for keyb, valueb in dicchangeb.items():
                if keya == keyb:
                    dicadd[keya] = valuea + valueb
                else:
                    dicadd[keya] = valuea
                    dicadd[keyb] = valueb
        p = 0
        for lendicadd in dicadd.items():
            p += 1
        addition = spars(p, 3)
        i = 0
        j = 0
        for keyadd in dicadd:
            addition.array_[i][2] = dicadd[keyadd]
            for digit in keyadd:
                addition.array_[i][j] = int(digit)
                j += 1
            i += 1
            j = 0
        return addition.array_, p

    def zarb(self, other, ka, kb):
        dicchangea = {}
        dicchangeb = {}
        diczarb = {}
        for ia in range(ka):
            for ja in range(1):
                dicchangea[str(self.array_[ia][ja]) + str(self.array_[ia][ja + 1])] = self.array_[ia][ja + 2]
        for ib in range(kb):
            for jb in range(1):
                dicchangeb[str(other.array_[ib][jb]) + str(other.array_[ib][jb + 1])] = other.array_[ib][jb + 2]
        z = 0
        for keya, valuea in dicchangea.items():
            for keyb, valueb in dicchangeb.items():
                if keya == keyb:
                    diczarb[keya] = valuea * valueb
                    z += 1
        zarb = spars(z, 3)
        i = 0
        j = 0
        for keyzarb in diczarb:
            zarb.array_[i][2] = diczarb[keyzarb]
            for digit in keyzarb:
                zarb.array_[i][j] = int(digit)
                j += 1
            i += 1
            j = 0
        return zarb.array_, z

    def zarbmatrix(self, other, i, jb, ka, kb):
        m = np.zeros((i * jb, 3), dtype=int)
        for i in range(kb):
            other.array_[i][0], other.array_[i][1] = other.array_[i][1], other.array_[i][0]
        zarbmatrix = []
        final = []
        for ja in range(ka):
            for jb in range(kb):
                if self.array_[ja][1] == other.array_[jb][1]:
                    zarbmatrix.append(
                        [self.array_[ja][0], other.array_[jb][0], self.array_[ja][2] * other.array_[jb][2]])
        l = 0
        while zarbmatrix != []:
            for first in zarbmatrix:
                row = first[0]
                column = first[1]
                refirst = first
                zarbmatrix.remove(first)
                for second in zarbmatrix:
                    if row == second[0] and column == second[1]:
                        final.append([row, column, refirst[2] + second[2]])
                        zarbmatrix.remove(second)
                        l += 1

                if l == 0:
                    final.append(first)
                    if len(zarbmatrix) != 1 and len(zarbmatrix) != 0:
                        final.append(second)
                    if len(zarbmatrix) == 0:
                        break
                    zarbmatrix.remove(second)
                l = 0

        return np.array(final)


a = spars()
b = spars()
print("please enter i and j for i * j matrix")
i = int(input('i:'))
j = int(input("j:"))
a.set_num(i, j, 'a')
issparsa, ka = a.is_spars(i, j)
b.set_num(i, j, 'b')
issparsb, kb = b.is_spars(i, j)
while True:
    if issparsa == True:
        achange = spars()
        achange.array_ = a.change(i, j, ka)
        print("kholase a: \n", achange.array_)
        break
    elif issparsa == False:
        print("--matrix is not spars please try again--")
        a.set_num(i, j, 'a')
        issparsa, ka = a.is_spars(i, j)

while True:
    if issparsb == True:
        bchange = spars()
        bchange.array_ = b.change(i, j, kb)
        print("kholase b :\n", bchange.array_)
        break
    elif issparsb == False:
        print("--matrix is not spars please try again--")
        b.set_num(i, j, 'b')
        issparsb, kb = b.is_spars(i, j)
reversespars = spars()
print("a main from kholase = \n", reversespars.reverse(achange.array_, i, j, ka))
print("b main from kholase = \n", reversespars.reverse(bchange.array_, i, j, kb))
add, p = achange.add(bchange, ka, kb)
print("a + b (kholase)= \n", add)
print("a + b (main from kholase) = \n", reversespars.reverse(add, i, j, p))
zarb, z = achange.zarb(bchange, ka, kb)
print("--zarb derayeyi-- a * b (kholase)= \n", zarb)
print("--zarb derayeyi-- a * b (main from kholase) = \n", reversespars.reverse(zarb, i, j, z))

c = input("if you want to calculate matrix multiply press 5 and enter if not press 0 and enter:")
if c == '5':
    while True:
        print("please enter i and j for first i * j matrix")
        i = int(input('i:'))
        ja = int(input("j:"))
        a.set_num(i, ja, 'a')
        issparsa, ka = a.is_spars(i, ja)
        if issparsa == True:
            achange = spars()
            achange.array_ = a.change(i, ja, ka)
            break
        if issparsa == False:
            print("This matrix is not spars please try again.")
    while True:
        print(f"please enter j for second {ja} * j matrix ")
        jb = int(input("j:"))
        b.set_num(ja, jb, 'b')
        issparsb, kb = b.is_spars(ja, jb)
        if issparsb == True:
            bchange = spars()
            bchange.array_ = b.change(ja, jb, kb)
            break
        if issparsb == False:
            print("This matrix is not spars please try again.")
    Z = spars()
    Z.array_ = achange.zarbmatrix(bchange, i, jb, ka, kb)
    print("kholase a*b(Matrix multiplication):\n", Z.array_)
else:
    exit(-1)
