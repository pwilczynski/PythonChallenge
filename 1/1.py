#!/usr/bin/env python

import string
alpha = string.ascii_lowercase
print alpha
f = open('basic.txt', 'r')
g = f.readlines()
for line in g:
	for word in line.split():
		new_word = ''
		for i in range(len(word)):
			 new_letter = (string.find(alpha, word[i])+2)%26
			 new_word= new_word + alpha[new_letter]
		#print new_word
		try: new_line = new_line + ' '+  new_word
		except: new_line = new_word
print new_line
