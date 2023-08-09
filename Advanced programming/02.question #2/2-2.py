def factoriel(x):
    if x == 0:
        return 1
    else:
        a = 1
        for F in range(1, x+1):
            a = a * F
    return a

def Mosalas (line):
    for line in range (0,line):
        a = factoriel(line)
        for i in range(0,line+1):
            b = factoriel(line-i)
            c = factoriel(i)
            d = b * c
            C = a // d
            print(end=str(C))
            print(end=" ")
            if line == 0:
                print()
            elif C == 1 and i != 0:
                print()

line = int(input("Please enter number of line : "))
Mosalas(line)