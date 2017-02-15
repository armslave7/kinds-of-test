##!/usr/bin/env python3

import itertools
import math


with open('mtsoft.dat','w') as fmt, open('in.dat') as fin:
        for line in fin:
                data=line.split()
                # print('%s %.4f %.3e' % (data[0],float(data[1]),float(data[2])))
                # print('%s %.6f %.3e %.3e %.3e %.3e' % (data[0],freq[i],float(data[2]),float(data[3]),float(data[2]),float(data[3])))
                # print('%s\n' %data[1])
                freq = math.log10(float(data[1]))
                fmt.write('%s %.8f %.3e %.3e %.3e %.3e 0\n' % (data[0],freq,float(data[2]),float(data[3]),float(data[4]),float(data[5])))
