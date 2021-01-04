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
num_arm = int(sys.argv[3])
mu_file = 'mu_' + str(num_arm) + '.txt'
avail_file = 'availability_' + str(num_arm) + '.txt'
ct_fl      = 'cost_' + str(num_arm) + '.txt'
mu = []
avl = []
cost = []
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

with open(ct_fl, 'r') as infile:
	for line in infile:
		cost.append(float(line))
cost = np.array(cost)

regret = {}
for i in range(T):
	regret[i] = 0

#alpha = 0.9
est_mu  = {}
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
		t_ucb =  np.multiply(A_t, ucb_val) - cost
		t_mu  =  np.multiply(A_t, mu) - cost
		#print (t_ucb, t_mu)
		#print("t_ucb", t_ucb)
		#Select all the arms (super-arm) with positive ucb - cost values (that is effective ucb) 
		S_t = []
		S_star = []
		for k in range(n):	
			if t_ucb[k] >=0:
				S_t.append(k)
			if t_mu[k] >= 0:
				S_star.append(k)
		#print (S_t, S_star)
		#print (I_t)
		#Reward
		cum_rew = 0
		opt_rew = 0
		for k in S_t:
			rew = np.random.binomial(1, mu[k])
			tot_rew[k] += rew
			num_pulls[k] += 1
			cum_rew += (mu[k] - cost[k])

		for k in S_star:
			opt_rew += (mu[k] - cost[k])

		#update
		for k in range(n):
			if num_pulls[k]!= 0:
				expl = (3* math.log10(i+1))/ (2*num_pulls[k]) 
				temp_ucb = tot_rew[k]/num_pulls[k] + math.sqrt(expl)
				ucb_val[k] = temp_ucb

		regret[i] += (opt_rew - cum_rew)
		#print (I_t, a_star, mu[I_t])
	est_mu[j] = ucb_val

	print(j)
	print("--- %s seconds ---" % (time.time() - start_time))
	start_time = time.time()

out = "out_k" + str(num_arm) + "_N" + str(N) + "_T" + str(T) + ".txt"
#out1 = "est_mu" + str(num_arm) + "_N" + str(N) + "_T" + str(T) + ".txt"
with open(out, 'w') as outfile:
	json.dump(regret, outfile)













