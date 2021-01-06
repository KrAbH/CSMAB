import numpy as np 
import matplotlib.pyplot as plt
import json
import matplotlib.patches as mpatches
import matplotlib
#matplotlib.rc('xtick', labelsize=11.5) 
#matplotlib.rc('ytick', labelsize=11.5)
matplotlib.rcParams.update({'figure.autolayout': True})
plt.tick_params(axis='both', which='major', labelsize=15)
out_fil = "regret_comp_Close.png"
N= 50

#k5 = "out_k5_N50_T1000000.txt"
k10 = "outTopK_k10_N50_K5_T1000000.txt"
k15 = "outTopK_k15_N50_K5_T1000000.txt"
k20 = "outTopK_k20_N50_K5_T1000000.txt"
k25 = "outTopK_k25_N50_K5_T1000000.txt"
k30 = "outTopK_k30_N50_K5_T1000000.txt"
k40 = "outTopK_k40_N50_K5_T1000000.txt"
k50 = "outTopK_k50_N50_K5_T1000000.txt"

files = [k10, k15, k20, k25, k30, k40, k50]
reg = []
####################################
for i in range(len(files)):

	with open(files[i], 'r') as infile:
		temp = json.load(infile)

	in1 = []
	for k, v in temp.items():
		in1.append(v)
	in1 = np.array(in1)/N
	in1 = np.cumsum(in1)
	reg.append(in1)
####################################
'''
b : blue.
g : green.
r : red.
c : cyan.
m : magenta.
y : yellow.
k : black.
w : white.

col = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

blue_patch = mpatches.Patch(color='blue', label='k = 5')
green_patch  = mpatches.Patch(color='green', label = 'k = 10')
red_patch  = mpatches.Patch(color='red', label = 'k = 15')
cyan_patch  = mpatches.Patch(color='cyan', label = 'k = 20')
magenta_patch  = mpatches.Patch(color='magenta', label = 'k = 25')
yellow_patch  = mpatches.Patch(color='yellow', label = 'k = 30')
black_patch  = mpatches.Patch(color='black', label = 'k = 40')
red_patch  = mpatches.Patch(color='red', label = 'k = 50')
#plt.legend(handles = [blue_patch, red_patch])
plt.
'''
plt.title('Regret Comparison (K=5)')
plt.ylabel('Regret')
plt.xlabel('Rounds(T)')
ind = []
for i in range(len(reg[0])):
	ind.append(i+1)

#plt.plot(ind, reg[0], label='k = 5')
plt.plot(ind, reg[0], label='k = 10')
plt.plot(ind, reg[1], label='k = 15')
plt.plot(ind, reg[2], label='k = 20')
plt.plot(ind, reg[3], label='k = 25')
plt.plot(ind, reg[4], label='k = 30')
plt.plot(ind, reg[5], label='k = 40')
plt.plot(ind, reg[6], label='k = 50')
plt.legend()

plt.savefig(out_fil)
