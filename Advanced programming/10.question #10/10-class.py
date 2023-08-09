class Goya:
    Numobject = 0
    def __init__( self, s, m):
        self.sorat = s
        self.makhraj = m
        numobject = Goya.Numobject + 1

    def jamgoya(self):
        mm = k1.makhraj * k2.makhraj
        b = []
        b.append(mm//k1.makhraj * k1.sorat)
        b.append(mm//k2.makhraj * k2.sorat)
        a = b[0] + b[1]
        n = 1
        return a,mm
    def tafrighgoya(self):
            mm = k1.makhraj * k2.makhraj
            b = []
            b.append(mm//k1.makhraj * k1.sorat)
            b.append(mm//k2.makhraj * k2.sorat)
            a = b[0] - b[1]
            n = 2
            return a,mm
    def zarbgoya(self):
        ss = k1.sorat * k2.makhraj
        mm = k1.makhraj * k2.sorat
        return ss,mm
    def taghsimgoya(self):
        ss = k1.sorat * k2.makhraj
        mm = k1.makhraj * k2.sorat
        return ss,mm
while True:
    while True:
        try:
            s = int(input("Lotfan sorat kasr aval ra vared konid : "))
            break
        except:
            print('LOTFAN ADD MORED NAZARETO VARED BOKON :(')
    while True:
        try:
            m = int(input("Lotfan makhraj kasr aval ra vared konid : "))
            break
        except:
            print('LOTFAN ADD MORED NAZARETO VARED BOKON :(')
    k1 = Goya(s, m)
    while True:
        try:
            s = int(input("Lotfan sorat kasr dovom ra vared konid : "))
            break
        except:
            print('LOTFAN ADD MORED NAZARETO VARED BOKON :(')
    while True:
        try:
            m = int(input("Lotfan makhraj kasr dovom ra vared konid : "))
            break
        except:
            print('LOTFAN ADD MORED NAZARETO VARED BOKON :(')
    k2 = Goya(s, m)
    print("====================================================")
    print("1-Agar "'"jam"'" do kasr ra mixahid add 1 ra vared konid")
    print("2-Agar "'"tafrigh"'" do kasr ra mixahid add 2 ra vared konid")
    print("3-Agar "'"zarb"'" do kasr ra mixahid add 3 ra vared konid")
    print("4-Agar "'"taghsim"'" do kasr ra mixahid add 4 ra vared konid")
    print("5-Agar mixahid az barname kharej shavid 0 ra vared konid")
    n = input("Lotfan entexab mored nazar khod ra vared konid : ")

    if n == '0':
        break
    elif n == '1':
        jamgoya = Goya(0,0)
        a,b = jamgoya.jamgoya()
        print("{}/{} + {}/{} = {}/{}".format(k1.sorat, k1.makhraj, k2.sorat, k2.makhraj, a, b))
    elif n == '2':
        tafrigh = Goya(0,0)
        a,b = tafrigh.tafrighgoya()
        print("{}/{} - {}/{} = {}/{}".format(k1.sorat, k1.makhraj, k2.sorat, k2.makhraj, a, b))
    elif n == '3':
        zarb = Goya(0,0)
        a,b = zarb.zarbgoya()
        print("{}/{} * {}/{} = {}/{}".format(k1.sorat, k1.makhraj, k2.sorat, k2.makhraj, a, b))
    elif n == '4':
        taghsim = Goya(0,0)
        a,b = taghsim.taghsimgoya()
        print("{}/{} ÷ {}/{} = {}/{}".format(k1.sorat, k1.makhraj, k2.sorat, k2.makhraj, a, b))

    E = input("Agar mixahid dobare emtehan konid ""1"" ra vared konid va agar mixahid az barname kharej shavid ""0"" ra vared konid : ")
    try:
        if E == "0":
            break
        if E == "1":
            print("---------------------------------------------------------")
    except:
        print("Lotfan ""1"" ya ""0"" vared konid")
    if E == "0" or n == "0":
        break