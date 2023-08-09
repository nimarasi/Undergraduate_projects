import matplotlib.pyplot as plt
import csv
import numpy as np

main_signal = []
noisy_signal = []

# function for clear noise
def clear_noise(noisy_list, n):
    cleared_noise = list()
    for i in range(int(n/2)):
        new_val = np.mean(noisy_list[:i + int(n / 2)])
        cleared_noise.append(new_val)


    for i in range(int(n/2), len(noisy_list) - int(n/2)):
        new_val = np.mean(noisy_list[i - int(n / 2) : i + int(n / 2) - 1])
        cleared_noise.append(new_val)


    return cleared_noise





# read main signal
with open('./main_signal.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')

    for row in lines:
        main_signal=row



for i in range(len(main_signal)):
    main_signal[i] = eval(main_signal[i])



# read noisy singnal
with open('./noisy_signal.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')

    for row in lines:
        noisy_signal=row

for i in range(len(noisy_signal)):
    noisy_signal[i] = eval(noisy_signal[i])

cleared_noise = list()
cleared_noise = clear_noise(noisy_signal, 30)


plt.plot(main_signal, color='r', label='main signal',linewidth=3)
plt.legend()
plt.figure()
plt.plot(noisy_signal, color='b', label='noisy signal')
plt.legend()
plt.figure()
plt.plot(cleared_noise,color='g', label='cleared noise')
plt.legend()
plt.show()

