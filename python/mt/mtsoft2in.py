##!/usr/bin/env python3

import itertools
import math

# freq=[]
# with open('freq.dat') as f:
# 	ite=itertools.islice(f,1,None)
# 	for line in ite:
# 		freq.append(float(line.strip()))
		#print(line.strip())

with open('in.dat','w') as fout, open('fre.dat','w') as fre:
        fre.write('\n')
        with open('mtsoft.dat') as ff:
                for line in ff:
                        data=line.split(' ')
                        # print('%s %.4f %.3e' % (data[0],float(data[1]),float(data[2])))
                        # print('%s %.6f %.3e %.3e %.3e %.3e' % (data[0],freq[i],float(data[2]),float(data[3]),float(data[2]),float(data[3])))
                        freq = math.pow(10,float(data[1]))
                        fout.write('%s %11.6f %.3e %.3e %.3e %.3e\n' % (data[0],freq,float(data[2]),float(data[3]),float(data[4]),float(data[5])))
                        fre.write('%11.6f\n' % freq)
