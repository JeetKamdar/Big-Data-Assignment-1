#!/usr/bin/env python

import sys
import os

current_key = None
current_count = 0

for line in sys.stdin:

	line = line.strip()
	key, count = line.split("\t", 1)

	try:
		count = int(count)
	except ValueError:
		continue

	if key == current_key:
		current_count += count
	else:
		if current_key:
			if (current_key[0] is "A"):
				print("vehicle_make\t%s, %d" % (current_key[1:],current_count))
			else: 
				print("vehicle_color\t%s, %d" % (current_key[1:], current_count))
		current_count = count
		current_key = key
if current_key == key:
	if (current_key[0] is "A"):
		print("vehicle_make\t%s, %d" % (current_key[1:], current_count))
	else:
		print("vehicle_color\t%s, %d" % (current_key[1:], current_count))
