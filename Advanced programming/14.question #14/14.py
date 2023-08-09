from numpy import *

class student:
    def __init__(self, name=None, id=None):
        self.name = name
        self.id = id

    def nameID(self, n):
        self.nameid = {}
        for i in range(n):
            name = input("name : ")
            id = int(input("Id : "))
            self.nameid[name] = id
        print("_______________________________")
    def Lesson(self,n):
        self.d = {}
        A =zeros((4,1))
        while n>0:
            print("*Nomarat Riyazi*")
            nameST = input("Lotfan name student ra vared konid :")
            for j in range(1):
                A[0][j] = float(input("Lotfan nomre ra vared konid : "))
            self.d[nameST] = A
            print("*Nomarat Fizik*")
            for j in range(1):
                A[1][j] = float(input("Lotfan nomre ra vared konid : "))
            self.d[nameST] = A
            print("*Nomarat Barnamesazi*")
            for j in range(1):
                A[2][j] = float(input("Lotfan nomre ra vared konid : "))
            self.d[nameST] = A
            print("*Nomarat Zaban*")
            for j in range(1):
                A[3][j] = float(input("Lotfan nomre ra vared konid : "))
            self.d[nameST] = A
            n -= 1
            if  n > 0:
                print("|*|Lotfan nomrat daneshjoye baadi ra vared konid|*|")
                A =zeros((4,1))
            else:
                c = input("agar mixahid dar nomarat edit anjam dahid 5 va enter bezanid dar gheyr in sorat fght enter bezanid:")
                if c == "5":
                    while True:
                        nameST = input("Lotfan name daneshjo ra vared konid :")
                        print("Riyazi = R , Fizik = F , BarnameSazi = B , Zaban = Z")
                        a = input("dar nomarat kodam dars mmixahid edit anjam dahid : ")
                        if a == "R":
                            for j in range(1):
                                A[0][j] = float(input("Lotfan nomre ra vared konid : "))
                            self.d[nameST] = A

                        if a == "F":
                            for j in range(1):
                                A[1][j] = float(input("Lotfan nomre ra vared konid : "))
                            self.d[nameST] = A
                        if a == "B":
                            for j in range(1):
                                A[2][j] = float(input("Lotfan nomre ra vared konid : "))
                            self.d[nameST] = A

                        if a == "Z":
                            for j in range(1):
                                A[3][j] = float(input("Lotfan nomre ra vared konid : "))
                            self.d[nameST] = A
                        e = input("agar mixahid dar nomarat edit anjam dahid 5 va enter bezanid dar gheyr in sorat fght enter bezanid :")
                        if e == "5":
                            continue
                        elif e!= "5":
                            break
                elif c != "5":
                    break
    def passORfail(self):
        for i in self.d.keys():
            SR = sum(self.d[i][0])
            AR = SR / 1
            SF = sum(self.d[i][1])
            AF = SF / 1
            SB = sum(self.d[i][2])
            AB = SB / 1
            SZ = sum(self.d[i][3])
            AZ = SZ / 1
            AT = (AR + AF + AB + AZ) / 4
            for j,value in self.nameid.items():
                if i == j and AT >= 10:
                        print()
                        print("student {} ba ID <{}> hame dars hara pass karde ast.".format(i,value))
                elif i == j and AT < 10:
                        print()
                        print("student {} ba ID <{}> mashrot shode ast.".format(i, value))


n = int(input("nomarat chand daneshjo ra mixahid vared konid :"))
a = student()
a.nameID(n)
a.Lesson(n)
a.passORfail()
