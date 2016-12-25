#!/usr/bin/env python3

import itertools

freq=[]
with open('freq.dat') as f:
	ite=itertools.islice(f,1,None)
	for line in ite:
		line.strip()
		freq.append(float(line))

with open('l800.dat') as f:
	i=0
	for line in f:
		data=line.split(' ')
		# print('%s %.4f %.3e' % (data[0],float(data[1]),float(data[2])))
		print('%s %.3f %.3e %.3e' % (data[0],freq[i%60],float(data[2]),float(data[3])))
		i=i+1