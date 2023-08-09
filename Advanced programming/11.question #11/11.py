from math import sqrt

class triangle():
    def __init__(self):
        self.am = 0
        self.h = 0

    def Mt(self, a):
        self.am = a
        self.Mt = self.am * 3
        return self.Mt
    def St(self, a, h):
        self.am = a
        self.h = h
        self.St = (self.am * self.h) // 2
        return self.St

class square():
    def __init__(self):
        self.as_ = 0

    def Ms(self, a):
        self.as_ = a
        self.Ms = self.as_ * 4
        return self.Ms
    def Ss(self, a):
        self.as_ = a
        self.Ss = self.as_ ** 2
        return self.Ss

class pyramid(triangle, square):
    def __init__(self):
        super().__init__()

    def Sp(self,am,as_,h):
        Sp = self.Ss(am) + self.St(as_,h) * 4
        return Sp

    def Vp(self,as_,Hp):
        Vp = self.Ss(as_) * Hp / 3
        Vp = "{:.2f}".format(Vp)
        return Vp
while True:
    print("**Lotfan yeki az gozine haye zir ra entexab konid** ")
    print("1- Mohit mosalas\n"
          "2- Masahat mosalas\n"
          "3- Mohit moraba\n"
          "4- Masahat moraba\n"
          "5- Mohit heram\n"
          "6- Hajm heram")
    n = int(input("Lotfan gozineye entexabi ra vared va enter ra bezanid : "))

    if n == 1:
        a = int(input("Lotfan zele mosalas ra vared konid : "))
        b = triangle()
        print("Mohit mosalas = ",end=str(b.Mt(a)))
    elif n == 2:
        a = int(input("Lotfan zele mosalas ra vared konid : "))
        h = int(input("Lotfan ertefa  mosalas ra vared konid : "))
        b = triangle()
        print("Masahat mosalas = ", end=str(b.St(a,h)))
    elif n == 3:
        a = int(input("Lotfan zele moraba ra vared konid : "))
        b = square()
        print("Mohit moraba = ", end=str(b.Ms(a)))
    elif n == 4:
        a = int(input("Lotfan zele moraba ra vared konid : "))
        b = square()
        print("Masahat moraba = ", end=str(b.Ss(a)))
    elif n == 5:
        am = int(input("Lotfan zele ghaede ra vared konid : "))
        as_ = int(input("Lotfan zele sathe janebi ra vared konid : "))
        h = int(input("Lotfan ertefa sathe janebi ra vared konid : "))
        b = pyramid()
        print("Masahat heram = ", end=str(b.Sp(am,as_,h)))
    elif n == 6:
        as_ = int(input("Lotfan zele ghaede ra vared konid : "))
        Hp = int(input("Lotfan zele sathe janebi ra vared konid : "))
        b = pyramid()
        print("Hajm heram = ", end=str(b.Vp(as_,Hp)))
    e = input("\nAgar mixahid az barname kharej shavid 0 ra vared karde va enter ra bezanid dar gheyr in sorat enter bezanid : ")
    if e == "0":
        break
    else:
        print("__________________________________________________________________________________")
        continue