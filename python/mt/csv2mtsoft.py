###!/usr/bin/env python3

import math
import csv
import itertools

with open('csvfiles') as ff:
	for line in ff:
		filename=line.strip()
		# print(filename)
		site=filename.rstrip('.csv')
		# print(filename,site)
		with open(filename) as f:
			reader=csv.DictReader(f)
			ite=itertools.islice(reader,1,None)
			for row in ite:
				freq=float(row['f(hz)'])
				rxy=float(row['Rhoxy ohm-m.'])
				phxy=float(row['PHASExy Deg.'])
				ryx=float(row['Rhoyx ohm-m.'])
				phyx=float(row['PHASEyx Deg.'])
				if abs(phxy)>90.0 :
					phxy=180-abs(phxy)
				else:
					phxy=abs(phxy)
				if abs(phyx)>90.0 :
					phyx=180-abs(phyx)
				else:
					phyx=abs(phyx)
				# print('%E %E'  % math.log10(freq) % row['Rhoxy ohm-m.'])
				print('%s %E %.3E %.3E %.3E %.3E %s'  %(site,math.log10(freq),rxy,phxy,ryx,phyx,'0'))


