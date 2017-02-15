#!/usr/bin/env python3

from itertools import *

with open('files') as ff:
	for line in ff:
		infilename=line.strip()
		file=infilename.rstrip('.txt')
		outfilename = file + '.dat'
		data=[]
		with open(infilename,'r') as f:
			ite=islice(f,1,None)
			for line in ite:
				line=line.strip()
				info=line.split()
				data.append(info)

		with open(outfilename,'w') as fe:
			step=0.025
			for i in range(10):
				for info in data:
					fe.write('%.3f' % (float(info[0])+i*step) )
					ite=islice(info,1,None)
					for dd in ite:
						fe.write("    "+dd)
					fe.write("\n")
