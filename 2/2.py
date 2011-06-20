#!/usr/bin/env python

import string
alpha = string.ascii_lowercase
print alpha
f = open('basic.txt', 'r')
g = f.readlines()
for line in g:
	for char in line:
		if char.isalpha():
			print char
