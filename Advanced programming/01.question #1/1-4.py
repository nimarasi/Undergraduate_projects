print("please enter 5 numbers : ")
b = []
for i in range(5):
    a = input()
    a = int(a)
    b.append(a)
print("halate aval : " , b)

b.sort()

print("pas az emal taghirat(min to max) : " , b)