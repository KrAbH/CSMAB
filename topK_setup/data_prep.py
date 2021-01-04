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
rs = 0.4
re = 0.7
mu_arr = np.random.uniform([rs]*k, [re]*k)
mu_file = 'mu_' + str(k) + '.txt'
with open(mu_file, 'w') as outfile:
	for i in mu_arr:
		outfile.write('%f\n' % i)

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




