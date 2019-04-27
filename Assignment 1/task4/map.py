#!/usr/bin/env python

import sys
import string
import re

for line in sys.stdin:

	line = line.strip()

	if '"' in line:
		entry = re.split(''',(?=(?:[^'"]|'[^']*'|"[^"]*")*$)''', line)
	else:
		entry = line.split(",")

	state = entry[-6].strip()

	#print ("%s\t1" % (state))
	print(state + "\t1")