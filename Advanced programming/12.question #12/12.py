class ab:
    def __init__(self,a,b):
        self.na = a
        self.nb = b
    def plus(self):
        pl = self.na + self.nb
        print("a + b =",pl)
    def power(self):
        po = self.na ** self.nb
        print("a ^ b =",po)
    def max(self):
        if self.na > self.nb:
            max = self.na
        elif self.nb > self.na:
            max = self.nb
        elif self.na == self.nb:
            max = self.na
        print("max =" ,max)

    def factoriel(self):
        f = 1
        i = 1
        while i <= self.nb:
            f = f * i
            i = i + 1
        print("factoriel b =",f)

while True:
    print("please enter 2 numbers below")
    a = int(input("first num :"))
    b = int(input("second num :"))
    c = ab(a,b)
    c.plus()
    c.power()
    c.max()
    c.factoriel()
    e = int(input("if you want to exit program press 0 and enter or if you want to continue press 5 and enter :"))
    if e != 0:
        print("==================================")
        continue
    else:
        break
