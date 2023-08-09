print("please enter 5 numbers : ")
b = []
for i in range(5):
    a = input()
    a = int(a)
    b.append(a)
print("halate aval : " , b)
for i in range(0, 4):
    for j in range(0,4):
        if b[j] > b[j + 1]:
            temp = b[j]
            b[j] = b[j + 1]
            b[j + 1] = temp

print("pas az emal taghirat(min to max) : " , b)