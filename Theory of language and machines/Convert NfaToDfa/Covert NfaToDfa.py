import numpy as np
List = []

def sort(sort_set):

    for i in range(1,len(sort_set)):
        for j in range(0,len(sort_set)-1):
            string1 = sort_set[j]
            state_num1 = string1[1:2]

            string2 = sort_set[j+1]
            state_num2 = string2[1:2]
            if state_num1 > state_num2:
                temp = string1
                sort_set[j] = string2
                sort_set[j+1] = temp
    return sort_set

def check_epsilon(s):

    result = findpath([s],'$')

    return result

def findpath(p, alphabet):
    row = 0
    column = 0
    for i in range(1, n + 1):
        if p == nfa[i][0]:
            row = i
            break
    for j in range(1, len(nfaalphabet) + 1):
        if alphabet == nfa[0][j]:
            column = j
            break

    if column == 0:
        return List
    if nfa[row][column] != None:
        for changetoList in nfa[row][column]:
            List.append(changetoList)

    return List


def check_NewState(q):
    for i in range(1, dfarow):
        if dfa[i][0] == q :
            return False

    return True



n = int(input("number of states : "))
nfaalphabet = []

# //// get alphabet
print("\n*** Enter alpahbet one by one instead of lambda enter $ when finish press Q *** ")
while True:
    a = input("enter : ")
    if a == 'Q':
        break
    nfaalphabet.append(a)

nfa = np.empty([n + 1, len(nfaalphabet) + 1], dtype=object)

a = []
for i in range(1, n + 1):
    a.append(f"q{i - 1}")
    nfa[i][0] = a.copy()
    a.clear()

for j in range(1, len(nfaalphabet) + 1):
    nfa[0][j] = f"{nfaalphabet[j - 1]}"

# /// get transactions and add to nfa matrix
a = []
for i in range(1, n + 1):
    for j in range(1, len(nfaalphabet) + 1):
        while (True):
            a0 = input(f"{nfa[i][0]} with {nfaalphabet[j - 1]} goes to : ")
            a.append(a0)
            if a0 == "":
                a.pop()
                if a != []:
                    nfa[i][j] = a.copy()
                a.clear()
                break


dfaalphabet = []

for checkNfaalphabet in nfaalphabet:
    if checkNfaalphabet == "$":
        continue
    else:
        dfaalphabet.append(checkNfaalphabet)

dfa = np.empty([2, len(dfaalphabet) + 1], dtype=object)

# find start state
for j in range(1, len(nfaalphabet) + 1):
    if nfa[0][j] == "$":
        if nfa[1][j] != None:
            dfa[1][0] = sort(list(set(nfa[1][0] + nfa[1][j])))
            for check_epsilon_for_dfa in nfa[1][j]:
              dfa[1][0] = sort(list(set(dfa[1][0] + check_epsilon(check_epsilon_for_dfa))))
            break

    if j == len(nfaalphabet):
        dfa[1][0] = nfa[1][0]

List.clear()
lenght_before = len(dfa[1][0])
lenght_after = len(dfa[1][0]) + 1

while(lenght_after != lenght_before):
    lenght_before = len(dfa[1][0])
    for check_epsilon_for_dfa in dfa[1][0]:
        dfa[1][0] = sort(list(set(dfa[1][0] + check_epsilon(check_epsilon_for_dfa))))
    lenght_after = len(dfa[1][0])

List.clear()

for j in range(1, len(dfaalphabet) + 1):
    dfa[0][j] = f"{dfaalphabet[j - 1]}"


newrow = np.empty([1, len(dfaalphabet) + 1], dtype=object)
finalpath = []

dfarow, dfacolumn = dfa.shape
check = False
d = 1
count = 0
i = 1
after_check = []
check_epsi = []
while (i < dfarow ):

    for j in range(1, dfacolumn):
        # if find new state add one row to dfa
        if dfa[i][dfacolumn - 1] != None and count == 1 and i < dfarow:
            count = 0
            i += 1
            for INewState in range(d, dfarow):
                for JNewState in range(1, dfacolumn):
                    check = check_NewState(dfa[INewState][JNewState])
                    if check:
                        dfa = np.vstack([dfa, newrow])
                        dfarow, dfacolumn = dfa.shape
                        dfa[dfarow - 1][0] = dfa[INewState][JNewState]

                d += 1
        if i == dfarow:
            break
        # peyda kardan masir haye yek ozv dar state va ejtema kardan
        index = dfa[i][0]
        if index != None:
            for state in index :
                check_epsi = findpath([state], dfa[0][j])
                for checkForepsi in check_epsi:
                    after_check = check_epsilon(checkForepsi)

                finalpath = sort(list(set(after_check)))


        dfa[i][j] = finalpath
        List.clear()
        finalpath = []
        if j == dfacolumn-1:
            count += 1
    dfarow, dfacolumn = dfa.shape

print("\n\n")

for i in range(1,dfarow):
    for j in range(1,dfacolumn):
        print(f"{dfa[i][0]} with {dfa[0][j]} --> {dfa[i][j]}\n")

