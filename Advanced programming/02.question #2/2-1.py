def specialnum(x):
    a = []
    for i in range(x):
         b = input()
         b = int(b)
         a.append(b)
    print("List aval : ", a)
    c = []
    for i in a:
       if i not in c:
           c.append(i)
    return c


x = int(input("How many numbers you want to enter? "))
c = specialnum(x)
print("List payani : " , c)