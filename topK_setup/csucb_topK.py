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
K = int(sys.argv[4])
mu_file = 'mu_' + str(num_arm) + '.txt'
avail_file = 'availability_' + str(num_arm) + '.txt'
#ct_fl      = 'cost_' + str(num_arm) + '.txt'
mu = []
avl = []
#cost = []
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

#alpha = 0.9
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
		t_ucb = []
		t_mu  = []
		for k in range(n):
			if A_t[k]==1:
				t1 = (ucb_val[k], k)
				t2 = (mu[k], k)
				t_ucb.append(t1)
				t_mu.append(t2)
				fl+= 1
		if fl <= K:
			regret[i] += 0
			print(i)
			continue

		#t_ucb =  np.multiply(A_t, ucb_val)
		#t_mu  =  np.multiply(A_t, mu)
		#print (t_ucb, t_mu)
		#print("t_ucb", t_ucb)
		#Select all the arms (super-arm) with positive ucb - cost values (that is effective ucb) 
		t_ucb.sort(reverse= True)
		t_mu.sort(reverse= True)
		#print (t_ucb, t_mu)
		S_t = []
		S_star = []
		for k in range(K):	
			i_t = t_ucb[k][1]
			S_t.append(i_t)
			i_str = t_mu[k][1]
			S_star.append(i_str)
		#print (S_t, S_star)
		#print (I_t)
		#Update 
		cum_rew = 0
		opt_rew = 0
		#print(S_t, S_star)
		for k in S_t:
			rew = np.random.binomial(1, mu[k])
			tot_rew[k] += rew
			num_pulls[k] += 1
			expl = (3* math.log(i+1, 2))/ (2*num_pulls[k]) 
			temp_ucb = tot_rew[k]/num_pulls[k] + math.sqrt(expl)
			ucb_val[k] = temp_ucb
			cum_rew += mu[k]

		for k in S_star:
			opt_rew += mu[k]
		
		#print ("S_star: ", S_star)
		#print ("S_t: ", S_t)
		#print(opt_rew - cum_rew)
		regret[i] += (opt_rew - cum_rew)
		#print (I_t, a_star, mu[I_t])
	print(j)
	print("--- %s seconds ---" % (time.time() - start_time))
	start_time = time.time()
	print(mu)
	print(ucb_val)
	print(num_pulls)
out = "outTopK_k" + str(num_arm) + "_N" + str(N) + "_K" + str(K) + "_T" + str(T) + ".txt"
with open(out, 'w') as outfile:
	json.dump(regret, outfile)











