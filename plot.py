import numpy as np
import matplotlib.pyplot as plt
import json

N = 1

infil = "out1.txt"

with open(infil, 'r') as infile:
	temp = json.load(infile)
reg = []
for k, v in temp.items():
	reg.append(v)
reg = np.array(reg)/N
reg = np.cumsum(reg)
ind = []
for i in range(len(reg)):
	ind.append(i+1)

plt.plot(ind, reg)
plt.xlabel('Rounds')
plt.ylabel('Regret')
plt.savefig('test.png', dpi=300)