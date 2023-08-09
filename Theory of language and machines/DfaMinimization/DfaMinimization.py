import numpy as np

def find(p,q):
    row = 0
    column = 0
    for i in range(1, n + 1):
        if A[i][0] == p:
            row = i
            break
    for j in range(1, n+1):
        if A[n][j] == q :
            column = j
            break
    return A[row][column]

def Distinct(p, q):
    flagp = False
    flagq = False
    for checkstate in finalstates:
        if p == checkstate:
            flagp = True
            break
    for checkstate in finalstates:
        if q == checkstate:
            flagq = True
            break
    if flagp != flagq:
        return True
    else:
        return False


def path(p, Funcalphabet):
    row = 0
    column = 0
    for i in range(1, n + 1):
        if B[i][0] == p:
            row = i
            break
    for j in range(1, len(alphabet) + 1):
        if B[0][j] == Funcalphabet:
            column = j
            break
    return B[row][column]


n = int(input("number of states : "))
alphabet = []
states = []
finalstates = []

# //// get alphabet
print("\n*** Enter alpahbet one by one when finish press Q *** ")
while True:
    a = input("enter : ")
    if a == 'Q':
        break
    alphabet.append(a)

# //// get and print states
for i in range(0, n):
    states.append("q{}".format(i))

print("States = "), print(states)

# //// get final states
print("*** Enter final states one by one when finish press Q --> example q0,q1,... ")

while True:
    a = input("enter : ")
    if a == 'Q':
        break
    finalstates.append(a)

# //// Make initial Transaction array
B = np.empty([n + 1, len(alphabet) + 1], dtype=object)

for i in range(1, n + 1):
    B[i][0] = f"q{i - 1}"

for j in range(1, len(alphabet) + 1):
    B[0][j] = f"{alphabet[j - 1]}"

# //// get Transactions
print("\nGive Transactions")
for j in range(1, len(alphabet) + 1):
    for i in range(1, n + 1):
        B[i][j] = input(f"{B[i][0]} with {B[0][j]} goes to : ")

# //// Make initial array
A = np.empty([n + 1, n + 1], dtype=object)
for i in range(0, n):
    for j in range(0, 1):
        A[i][j] = f"q{i}"

for i in range(n, n + 1):
    for j in range(1, n + 1):
        A[i][j] = f"q{j - 1}"

# //// find Distinct states 
d = 1
while (d < n):
    for i in range(d, d + 1):
        for j in range(1, d + 1):
            if Distinct(A[i][0], A[n][j]):
                A[i][j] = '$'
        d += 1


flag = True
count = 0
d = 1

while (flag):
    while (d < n):
        for check_alphabet in alphabet:
            for i in range(d, d + 1):
                for j in range(1, d + 1):
                    a = find(path(A[i][0], check_alphabet),path(A[n][j], check_alphabet))
                    b = find(path(A[n][j], check_alphabet) , path(A[i][0], check_alphabet))
                    if A[i][j] == None and (a != None or b != None):
                        A[i][j] = check_alphabet
                        count += 1
        d += 1
        if i == n - 1 and j == d -1 and count == 0:
            flag = False
        elif i == n - 1 and j == d -1 and count != 0:
            count = 0
            d = 1


mergeStates = []
d = 1
while (d < n):
    for i in range(d, d + 1):
        for j in range(1, d + 1):
            if A[i][j] == None :
                mergeStates.append(f"{A[i][0]},{A[n][j]}")
    d += 1

print("\nAll states : ")
print(states)
print("\nFinal states : ")
print(finalstates)
print("\nMerge States : ")
print(mergeStates)

