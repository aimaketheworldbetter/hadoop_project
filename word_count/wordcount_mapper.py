#!/usr/bin/python
import sys
#read from input
for line in sys.stdin:
	for word in line.strip().split():
		print '%s\t%d' %(word, 1)
