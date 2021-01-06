import numpy as np
import random 
import math
from scipy.stats import bernoulli
import sys
import json

#k: Number of arms
k = int(sys.argv[1])

########################################################################
#Reward true mean
#range within which true mu belongs
delta = 0.001 #this is \sqrt(1/T), when T = 1M
rs = 0.5
re = 0.6
mu_arr = np.random.uniform([rs]*k, [re]*k)
mu_file = 'mu_' + str(k) + '.txt'
with open(mu_file, 'w') as outfile:
	for i in range(k):
		outfile.write('%f\n' % rs)
		rs += delta
    

########################################################################

########################################################################
#Availability mean
#range within which mean belongs
rs = 0.6
re = 0.9
mu_arr = np.random.uniform([rs]*k, [re]*k)
mu_file = 'availability_' + str(k) + '.txt'
with open(mu_file, 'w') as outfile:
	for i in mu_arr:
		outfile.write('%f\n' % i)

########################################################################




