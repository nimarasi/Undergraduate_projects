import numpy as np

n = int(input("Please enter number of process : "))

T = []

for i in range(1, n + 1):
    e = int(input("enfejar{} : ".format(i)))
    v = int(input("vorod{} : ".format(i)))
    T.append([i, e, v])

print("T : [process No , enfejar , vorod ]")
print("T : \n", T)

# //////////////////////////////// << FCFS >>


fcfs = sorted(T, key=lambda x: (x[2]))
print("FCFS : ", fcfs)
Sum = 0
k = 0
fcfsgant = [0]

for i in range(0, n):
    for j in range(0, k + 1):
        Sum = fcfs[j][1] + Sum
    k += 1
    fcfsgant.append(Sum)
    Sum = 0
print("FCFS Gant : ", fcfsgant)

fcfsEntezar = []
fcfsBargasht = []

for i in range(0, n):
    fcfsEntezar.append([fcfs[i][0], fcfsgant[i] - fcfs[i][2]])
    fcfsBargasht.append([fcfs[i][0], fcfsgant[i + 1] - fcfs[i][2]])

print("FCFS Entezar : ", fcfsEntezar)
print("FCFS Barghast : ", fcfsBargasht)

SumEntezar = 0
SumBarghast = 0
for i in range(0, n):
    SumEntezar = fcfsEntezar[i][1] + SumEntezar
    SumBarghast = fcfsBargasht[i][1] + SumBarghast

print("Avg FCFS Entezar : " , SumEntezar/n)
print( "Avg FCFS Bargasht : ", SumBarghast/n)

print("___________________________________")


# //////////////////////////

# /////////////////////////  << SJF >>

sorted_sjf = sorted(T, key=lambda x: (x[2]))

sjf = []
sjfgant = [0]
sjf_lowExecute = []
execute = [[0,1000,0]]
timer = 0
moving = 0


while len(sjf) != n :

        while True:
            if moving == len(sorted_sjf) :
                break
            if timer >= sorted_sjf[moving][2]:
                sjf_lowExecute.append(sorted_sjf[moving])
                sorted_sjf.pop(moving)
                moving = 0
            else:
                moving += 1


        for k in range(0,len(sjf_lowExecute)):
            if sjf_lowExecute[k][1] <= execute[0][1]:
                execute = [sjf_lowExecute[k]]
                k1 = k

        sjf.append(sjf_lowExecute[k1])
        sjf_lowExecute.pop(k1)
        moving = 0
        timer = execute[0][1]
        execute = [[0,1000,0]]
        sjfgant.append(sjfgant[len(sjfgant)-1] + timer)
        timer = sjfgant[len(sjfgant)-1]

print("SJF : ", sjf)
print("sjf Gant : ", sjfgant)

sjfEntezar = []
sjfBargasht = []

for i in range(0, n):
    sjfEntezar.append([sjf[i][0], sjfgant[i] - sjf[i][2]])
    sjfBargasht.append([sjf[i][0], sjfgant[i + 1] - sjf[i][2]])

print("SJF Entezar : ", sjfEntezar)
print("SJF Barghast : ", sjfBargasht)

SumEntezar = 0
SumBarghast = 0
for i in range(0, n):
    SumEntezar = sjfEntezar[i][1] + SumEntezar
    SumBarghast = sjfBargasht[i][1] + SumBarghast

print("Avg SJF Entezar : " , SumEntezar/n)
print( "Avg SJF Bargasht : ", SumBarghast/n)

print("___________________________________")

# ///////////////////////

# ////////////////////// << SRTF >>


sorted_srtf = sorted(T, key=lambda x: (x[2]))

srtf = []
srtfgant = [0]

srtf_lowExecute = []
execute = [[0, 1000, 0]]
timer = 0
moving = 0
max_execute = 0

for i in range(0, n):
    if sorted_srtf[i][1] > max_execute:
        max_execute = sorted_srtf[i][1]

while True:
    while True:
        if moving == len(sorted_srtf):
            break
        if timer >= sorted_srtf[moving][2]:
            srtf_lowExecute.append(sorted_srtf[moving].copy())
            sorted_srtf.pop(moving)
            moving = 0
        else:
            moving += 1

    for k in range(0, len(srtf_lowExecute)):
        if srtf_lowExecute[k][1] <= execute[0][1]:
            execute = [srtf_lowExecute[k]]
            k1 = k

    temp = srtf_lowExecute[k1][1]
    temp = temp - 1
    srtf_lowExecute[k1][1] = temp
    srtf.append(srtf_lowExecute[k1].copy())

    if srtf_lowExecute[k1][1] == 0:
        srtf_lowExecute.pop(k1)
    if len(srtf_lowExecute) == 0 and len(sorted_srtf) == 0:
        break
    moving = 0
    timer += 1
    execute = [[0, 1000, 0]]

a = srtf[0][0]
srtf_test = []
for i in range(0, len(srtf) + 1):
    if i == len(srtf) and a == srtf[i - 1][0]:
        srtfgant.append(i)
        srtf_test.append("p{}".format(srtf[i - 1][0]))
        break
    if a != srtf[i][0]:
        srtfgant.append(i)
        srtf_test.append("p{}".format(srtf[i - 1][0]))
        a = srtf[i][0]

print("SRTF(dar har saniye) : ", srtf)
print("SRTF : ", srtf_test)
print("srtf Gant : ", srtfgant)

srtfEntezar = []
srtfBargasht = []

srtfEntezar.append([srtf_test[0], srtfgant[0]])

for i in range(0, len(srtf_test)):
    a = srtf_test[i]
    for j in range(i-1,-1,-1):
        b = srtf_test[j]
        if a == b:
            srtfEntezar.append([srtf_test[j], srtfgant[i] - srtfgant[j+1]])
            break
        elif j == 0 :
            srtfEntezar.append([srtf_test[i], srtfgant[i] - T[int(srtf_test[i][1]) - 1 ][2]])

srtfEntezar_payani = []
a = 0

for i in range(0,n):
    for j in range(0,len(srtfEntezar)):
        if srtfEntezar[j][0] == 'p{}'.format(i+1):
            a = a + srtfEntezar[j][1]
    srtfEntezar_payani.append(['p{}'.format(i+1) ,a])
    a = 0


for i in range(0,n):
    for j in range(0,len(srtfEntezar)):
        if srtf_test[j] == 'p{}'.format(i+1):
            a = j
    srtfBargasht.append(['p{}'.format(i+1) ,srtfgant[a+1] - T[i][2]])
    a = 0


print("SRTF Entezar : ", srtfEntezar_payani)
print("SRTF Barghast : ", srtfBargasht)

SumEntezar = 0
SumBarghast = 0

for i in range(0, n):
    SumEntezar = srtfEntezar_payani[i][1] + SumEntezar
    SumBarghast = srtfBargasht[i][1] + SumBarghast

print("Avg SRTF Entezar : {:.2f}".format(SumEntezar / n))
print("Avg SRTF Bargasht : {:.2f}".format(SumBarghast / n))

print("___________________________________")

# //////////////////////////

# //////////////////////////   << RR >>

sorted_rr = sorted(T, key=lambda x: (x[2]))

time_quantum = int(input("please enter time Quantum : "))

rr = []
rrgant = [0]
rr_Execute = []
a = sorted_rr[0][0] - 1
b = 1
timer = 0
moving = 0
flag = False
sortExecute_flag = False

while len(sorted_rr) != 0:

    while True:
        if moving == len(sorted_rr):
            break
        if timer >= sorted_rr[moving][2]:
            rr_Execute.append(sorted_rr[moving].copy())
            sorted_rr.pop(moving)
            moving = 0
        else:
            moving += 1

    for i in range(0, len(rr_Execute)):
        if i + 1 > a:
            for j in range(0, len(rr_Execute)):
                if rr_Execute[j][1] >= time_quantum and i + 1 == rr_Execute[j][0]:
                    rr_Execute[j][1] = rr_Execute[j][1] - time_quantum
                    timer = timer + time_quantum
                    rr.append("p{}".format(rr_Execute[j][0]))
                    rrgant.append(timer)
                elif rr_Execute[j][1] < time_quantum and rr_Execute[j][1] != 0 and i + 1 == rr_Execute[j][0]:
                    timer = timer + rr_Execute[j][1]
                    rr_Execute[j][1] = 0
                    rr.append("p{}".format(rr_Execute[j][0]))
                    rrgant.append(timer)
            break

    for i in range(len(rr_Execute), 0, -1):
        sorted_rr.append(rr_Execute[i - 1])

    sorted_rr = sorted(sorted_rr, key=lambda x: (x[2]))
    rr_Execute = []
    moving = 0

    if a == n - 1:
        a = T[0][0] - 1
        b = 1
    else:
        a = T[b][0] - 1
        b += 1

    for i in range(0, len(sorted_rr)):
        if sorted_rr[i][1] != 0:
            flag = False
            break
        if sorted_rr[i][0] == len(sorted_rr):
            flag = True
    if flag:
        break

print("RR : ", rr)
print("rr Gant : ", rrgant)

rrEntezar = []
rrBargasht = []

rrEntezar.append([rr[0], rrgant[0]])

for i in range(0, len(rr)):
    a = rr[i]
    for j in range(i - 1, -1, -1):
        b = rr[j]
        if a == b:
            rrEntezar.append([rr[j], rrgant[i] - rrgant[j + 1]])
            break
        elif j == 0:
            rrEntezar.append([rr[i], rrgant[i] - T[int(rr[i][1]) - 1][2]])

rrEntezar_payani = []
a = 0

for i in range(0, n):
    for j in range(0, len(rrEntezar)):
        if rrEntezar[j][0] == 'p{}'.format(i + 1):
            a = a + rrEntezar[j][1]
    rrEntezar_payani.append(['p{}'.format(i + 1), a])
    a = 0


for i in range(0, n):
    for j in range(0, len(rrEntezar)):
        if rr[j] == 'p{}'.format(i + 1):
            a = j
    rrBargasht.append(['p{}'.format(i + 1), rrgant[a + 1] - T[i][2]])
    a = 0

print("RR Entezar : ", rrEntezar_payani)
print("RR Barghast : ", rrBargasht)

SumEntezar = 0
SumBarghast = 0

for i in range(0, n):
    SumEntezar = rrEntezar_payani[i][1] + SumEntezar
    SumBarghast = rrBargasht[i][1] + SumBarghast

print("Avg RR Entezar : {:.2f}".format(SumEntezar / n))
print("Avg RR Bargasht : {:.2f}".format(SumBarghast / n))

