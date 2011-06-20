#!/usr/bin/env python

import string
               

def check_string( st ):
	#this function checks if a string is what we want it to be, if not, it returns
	#lUUUlUUUl
	fail = 0
	#print st
	upper = [1,2,3,5,6,7]
	lower = [0,4,8]
	for i in upper:
		if st[i].islower():
			fail = 1
			break
		else:
			continue
	if fail == 1:
		return
	for i in lower:
		if st[i].isupper():
			fail = 1
			break
		else:
			continue
	if fail == 0:
		print st[4]
		return
	else: 
		return
f = open('basic.txt', 'r')
g = f.readlines()
position = 0
for line in g:
	line = line.rstrip('\r\n')
	line = 'a' + line + 'a'
	for i in range(len(line[:-8])):
		check_string(line[i:i+9])
