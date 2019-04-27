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

	color, make = entry[-3:-1]
	
	if color is "":
		color = "NONE"
	if make is "":
		make = "NONE"

	print("A%s\t1" % make.replace('"',''))
	print("Z%s\t1" % color.replace('"',''))
