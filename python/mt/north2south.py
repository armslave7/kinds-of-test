#!/usr/bin/env python3

from itertools import *

point=5200
outfilename="n2s%4i.txt" %(point)
postfile="n2s%4ipost.dat" %(point)
blnfile="n2s%4i.bln" %(point)
point = point/1000.0
str_pt = "%.3f" % (point)
hight=-10.0
bln=[]

with open('files','r') as ff, open(outfilename,'w') as fout, open(postfile,'w') as fp:
    for fline in ff:
        infilename=fline.strip()
        site=infilename.rstrip('.txt')
        site=int(site)
        site = site/1000

        with open(infilename,'r') as f:
            ite=islice(f,1,None)
            tag=True
            for line in ite:
                lll=line.strip()
                data=lll.split()
                if(str_pt == data[0]):
                    if(tag):
                        # fbln.write("%.3f  %s\n" %(site,data[1]) )
                        if(float(data[1])>hight):
                            hight=float(data[1])
                        bln.append((site,data[1]))
                        fp.write("%.3f  %s\n" %(site,data[1]) )
                        tag=False
                    fout.write("%.3f   %s   %s   %s\n" % (site,data[1],data[2],data[3]) )

print(len(bln))
inda = (bln[0][0],hight+0.1)
bln.insert(0,inda)
indb = (bln[len(bln)-1][0],hight+0.1)
bln.append(indb)
bln.append(inda)


with open(blnfile,'w') as fbln:
    fbln.write("%2i  1\n" %(len(bln)))
    for site,dd in bln:
        fbln.write("%.3f   %s\n" %(site,dd) )
