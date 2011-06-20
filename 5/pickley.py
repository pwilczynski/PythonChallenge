#!/usr/bin/env python
#downloads x-ray diffraction data from eds

import urllib2, sys, string,pickle

f = open('banner.p', 'r')
pickled = pickle.load(f)
for i in pickled:
    print i

f2 = open('out','w')
for i in pickled:
	for j in i:
		f2.write(j[0]*j[1])
		f2.write("\n")
f2.close()
