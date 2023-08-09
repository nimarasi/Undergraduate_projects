print("number of Process : ")
P = int(input())
print("number of Resource : ")
R = int(input())


def calculateNeed(need, maxm, allot):
    for i in range(P):
        for j in range(R):
            need[i][j] = maxm[i][j] - allot[i][j]


def isSafe(processes, avail, maxm, allot):
    need = []
    for i in range(P):
        l = []
        for j in range(R):
            l.append(0)
        need.append(l)
    calculateNeed(need, maxm, allot)
    finish = [0] * P
    safeSeq = [0] * P
    work = [0] * R
    for i in range(R):
        work[i] = avail[i]
    count = 0
    while (count < P):
        found = False
        for p in range(P):
            if (finish[p] == 0):
                for j in range(R):
                    if (need[p][j] > work[j]):
                        break
                if (j == R - 1):
                    for k in range(R):
                        work[k] += allot[p][k]
                    safeSeq[count] = p
                    count += 1

                    finish[p] = 1

                    found = True
        if (found == False):
            print("System is not in safe state.")
            return False
    print("System is in safe state.")
    return True

processes = []
for i in range(0, P):
    processes.append(i)

print("avail : ")
avail = list(map(int, input().split()))

print("maxm : ")
maxm = [list(map(int,input().split())) for i in range(P)]

print("allot : ")
allot = [list(map(int,input().split())) for i in range(P)]

isSafe(processes, avail, maxm, allot)

print("taghaza : ")
user = list(map(int, input().split()))
user1 = []
counter = 0
for i in user:
    if counter != 0:
        user1.append(i)
    counter = counter + 1
s = allot.pop(user[0])
res_list = [s[i] + user1[i] for i in range(len(s))]
allot.insert(user[0],res_list)
isSafe(processes, avail, maxm, allot)


