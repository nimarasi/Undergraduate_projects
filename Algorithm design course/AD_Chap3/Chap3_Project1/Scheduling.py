import numpy as np

n = int(input("How many works you want to enter : "))

swaplist = []
l = []
t = 0
b = 0
"""
input jobs deadline and profits
"""
for i in range(0, n):
    t = int(input("enter time : "))
    b = int(input("bahre : "))
    l.append([i + 1 , t ,b])

"""
sort jobs with max profit
"""
for i in range(0,n):
    for j in range (0,n):
        if l[i][2] > l[j][2] :
            swaplist = l[i].copy()
            l[i] = l[j]
            l[j] = swaplist

print("\nSorted jobs with profit : ")
print(l)

"""
find max job deadline
"""
maxtime = 0
for i in range(0, n):
    if maxtime < l[i][1]:
        maxtime = l[i][1]
# print(maxtime)
sloution = []
for i in range(0,maxtime):
    sloution.append([])

n = 0
count = 0

while(n < len(l) ):
        flag = True
        if sloution[l[n][1] - 1] == []:
            sloution[l[n][1] - 1] = l[n]
            l.remove(l[n])
            n = 0
            flag = False
        else:
            for j2 in range(l[n][1] - 1 , 0 , -1):
                if sloution[l[j2][1] - 1 ]== []:
                    sloution[l[j2][1] - 1] = l[n]
                    l.remove(l[j2])
                    n = 0
                    flag = False
        for i in range(0,maxtime):
            if sloution[i] == []:
                count += 1
                break
        if count == 0:
            break
        if flag :
            n += 1
            count = 0


print("\nFinal anwser : ", sloution)
Sum = 0
for i in range(0,maxtime):
    Sum = Sum + sloution[i][2]
print("\nTotal profit : ",Sum)

