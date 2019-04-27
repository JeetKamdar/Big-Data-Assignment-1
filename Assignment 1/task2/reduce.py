#!/usr/bin/env python

import sys

current_code = None
current_count = 0
code = None

for line in sys.stdin:
	line = line.strip()
	code, count = line.split("\t")
	try:
		count = int(count)
	except ValueError:
		continue

	if code == current_code:
		current_count += count
	else:
		if current_code:
			print("%s\t%d" % (current_code, current_count))
		current_code = code
		current_count = count

if current_code == code:
	print("%s\t%d" % (current_code,current_count))