import numpy as np
import random 
import math
from scipy.stats import bernoulli
import sys
import json
import matplotlib.pyplot as plt
import time

start_time = time.time()
N = int(sys.argv[1]) #N is number of epochs
T = int(sys.argv[2]) #T is number of rounds in one epoch
mu_file = 'mu.txt'
avail_file = 'availability.txt'
mu = []
avl = []
n =0 
with open(mu_file, 'r') as infile:
	for line in infile:
		n += 1 #n is number of arms
		mu.append(float(line))

mu = np.array(mu)
with open(avail_file, 'r') as infile:
	for line in infile:
		avl.append(float(line))

avl = np.array(avl)

regret = {}
for i in range(T):
	regret[i] = 0

alpha = 0.9
for j in range(N):
	
	num_pulls = np.zeros(n, dtype = float)
	tot_rew    = np.zeros(n, dtype = float)
	#expl_term = np.zeros(n, dtype = float)
	ucb_val   = []
	t = 99999999
	#Intializing the ucb values with large number so that if the arm is not pulled 
	for i in range(n):
		ucb_val.append(t)

	for i in range(T):
		#Generate the availability of arms considering it as bernoulli random variable
		#print ("ucb_val", ucb_val)

		A_t  = np.random.binomial(1, avl)
		#print("A_t", A_t)
		#print (type(A_t), A_t)
		fl = 0
		for k in range(n):
			if A_t[k]==1:
				fl=1
				break
		if fl==0:
			regret[i] += 0
			continue
		t_ucb =  np.multiply(A_t, ucb_val)
		t_mu  =  np.multiply(A_t, mu)
		#print("t_ucb", t_ucb)
		#Find the index of arm with max ucb value
		mx_ind = -1
		mx = -100000
		for k in range(n):	
			if mx < t_ucb[k]:
				mx = t_ucb[k]
				mx_ind = k
		I_t = mx_ind
		#print (I_t)
		rew = np.random.binomial(1, mu[I_t])
		#Update 
		tot_rew[I_t] += rew
		num_pulls[I_t] += 1
		for k in range(n):
			if num_pulls[k]!=0:
				expl = (3* math.log10(i+1))/ (2*num_pulls[I_t]) 
				temp_ucb = tot_rew[I_t]/num_pulls[I_t] + math.sqrt(expl)
				ucb_val[I_t] = temp_ucb

		a_star = np.amax(t_mu)
		regret[i] += a_star - mu[I_t]
		#print (I_t, a_star, mu[I_t])
	print(j)
	print("--- %s seconds ---" % (time.time() - start_time))
	start_time = time.time()

out = "out1.txt"
with open(out, 'w') as outfile:
	json.dump(regret, outfile)











