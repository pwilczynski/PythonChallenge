#!/usr/bin/env python
#downloads x-ray diffraction data from eds

import urllib2, sys, string
next_num = '8022'

for i in range(500):
	f = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+next_num)
	html = f.read() 
	next_num = html.split()[-1]
	print html
