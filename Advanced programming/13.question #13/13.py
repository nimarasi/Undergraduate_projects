class huge_int():
    def __init__(self, number='0'):
        self.num = number

    def set_num(self, name):
        self.num = input(f'please enter {name} : ')

    def __lt__(self, other):
        if self.num[0] != '-' and other.num[0] != '-':
            if len(self.num) > len(other.num):
                return '>'
            elif len(self.num) < len(other.num):
                return '<'
            if len(self.num) == len(other.num):
                for i, j in zip(self.num, other.num):
                    if i > j:
                        return '>'
                    if i < j:
                        return '<'
            if len(self.num) == len(other.num):
                return '='
        if self.num[0] == '-' and other.num[0] == '-':
            if len(self.num) > len(other.num):
                return '<'
            elif len(self.num) < len(other.num):
                return '>'
            if len(self.num) == len(other.num):
                for i, j in zip(self.num, other.num):
                    if i > j:
                        return '<'
                    if j > i:
                        return '>'
            if len(self.num) == len(other.num):
                return '='

    def __add__(self, other):
        if len(self.num) < len(other.num):
            self.num, other.num = other.num, self.num
        self.num = self.num[::-1]
        other.num = other.num[::-1]
        k = 0
        add = ''
        for char in range(len(self.num)):
            try:
                i = self.num[char]
                j = other.num[char]
                i = ord(i) - 48
                j = ord(j) - 48
                plus = i + j + k
                k = 0
            except:
                i = self.num[char]
                i = ord(i) - 48
                plus = i + 0 + k
                k = 0
            while plus >= 10:
                plus -= 10
                k += 1
            add = str(plus) + add
        if k != 0:
            add = str(k) + add
            k = 0
        self.num = self.num[::-1]
        other.num = other.num[::-1]
        return add

    def minus(self, other):
        compare = self.__lt__(other)
        if compare == "<":
            self.num, other.num = other.num, self.num
        self.num = self.num[::-1]
        other.num = other.num[::-1]
        k = 0
        remove = huge_int('')
        for char in range(len(self.num)):
            try:
                i = self.num[char]
                j = other.num[char]
                i = ord(i) - 48
                j = ord(j) - 48
                minus = i - j - k
                k = 0
            except:
                i = self.num[char]
                i = ord(i) - 48
                minus = i - 0 - k
                k = 0
            while minus < 0:
                minus -= 10
                k += 1
            remove.num = str(minus) + remove.num
        if k != 0:
            remove.num = str(k) + remove.num
            k = 0
        self.num = self.num[::-1]
        other.num = other.num[::-1]
        return remove

    def zarb(self, other):
        compare = self.__lt__(other)
        if compare == "<":
            self.num, other.num = other.num, self.num
        add = huge_int('')
        k = 0
        zero = 0
        z = huge_int('')
        self.num = self.num[::-1]
        other.num = other.num[::-1]
        for j in other.num:
            j = ord(j) - 48
            for i in self.num:
                i = ord(i) - 48
                multi = i * j + k
                k = 0
                while multi >= 10:
                    multi -= 10
                    k += 1
                add.num = str(multi) + add.num
            if k != 0:
                add.num = str(k) + add.num
                k = 0
            zero += 1
            if zero > 1:
                for zeroo in range(zero - 1):
                    add.num = add.num + '0'
            z.num = z.__add__(add)
            add.num = ''
        if compare == "<":
            self.num, other.num = other.num, self.num
        self.num = self.num[::-1]
        other.num = other.num[::-1]
        return z.num

    def fac(self):
        i = huge_int('1')
        j = huge_int('1')
        z = huge_int('1')
        if self.num == '0' or self.num == '1':
            return '1'
        else:
            while True:
                i.num = i.zarb(j)
                j.num = j + z
                compare = j > self
                if compare == "<":
                    break
            return i.num

    def Tavan(self, power=0):
        result = huge_int('1')
        for pow_ in range(power):
            result.num = result.zarb(self)
        return result.num

a = huge_int()
b = huge_int()
a.set_num('a')
b.set_num('b')
print(f"A {a.__lt__(b)} B")
print(f"a+b = {a.__add__(b)}")
print(f"a*b = {a.zarb(b)}")
print(f"a! = {a.fac()}")
print(f"b! = {b.fac()}")
power = int(input(f"please enter power : "))
print(f"a^{power} = {a.Tavan(power)}")
print(f"b^{power} = {b.Tavan(power)}")
