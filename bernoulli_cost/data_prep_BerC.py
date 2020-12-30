import numpy as np
import random 
import math
from scipy.stats import bernoulli
import sys
import json

#k: Number of arms
k = 15

########################################################################
#Reward true mean
#range within which true mu belongs
rs = 0.2
re = 0.9
mu_arr = np.random.uniform([rs]*k, [re]*k)
mu_file = 'mu.txt'
with open(mu_file, 'w') as outfile:
	for i in mu_arr:
		outfile.write('%f\n' % i)

########################################################################

########################################################################
#Availability mean
#range within which mean belongs
rs = 0.3
re = 0.7
mu_arr = np.random.uniform([rs]*k, [re]*k)
mu_file = 'availability.txt'
with open(mu_file, 'w') as outfile:
	for i in mu_arr:
		outfile.write('%f\n' % i)

########################################################################

########################################################################
#Availability mean
#range within which mean belongs
rs = 0.3
re = 0.7
mu_arr = np.random.uniform([rs]*k, [re]*k)
mu_file = 'cost.txt'
with open(mu_file, 'w') as outfile:
	for i in mu_arr:
		outfile.write('%f\n' % i)

########################################################################