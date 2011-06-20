#!/usr/bin/env python

import string

f = open('basic.txt', 'r')
g = f.readlines()

for line in g:
	#print line
	for char in line:
		if char.islower():
			char_index = line.find(char)
			n_caps=0
        	if (char_index >= 3) and (char_index <= (len(line)-4)):
				#print line[char_index-3:char_index] +' ' + char + ' '+ line[char_index + 1:char_index+4]
				for i in line[char_index-3:char_index+4]:
					n_caps = n_caps+ i.isupper()
					#print i, n_caps
				if n_caps == 6:
					#check surrounding letters
					if char_index >= 4:
						n_caps = n_caps + line[char_index-4].isupper()
					if char_index <= len(line)-5:
						n_caps = n_caps + line[char_index+4].isupper()
					if n_caps == 6:
						print line[char_index-4:char_index+5]
						print line[char_index]
				n_caps = 0
		else:
			continue
