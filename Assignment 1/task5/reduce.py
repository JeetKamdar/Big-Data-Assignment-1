#!/usr/bin/env python

import sys
import string

current_key = None
current_count = 0
highest_count_key = None
highest_count = 0

for line in sys.stdin:

	line = line.strip()
	key,count = line.split("\t")

	try:
		count = int(count)
	except ValueError:
		continue

	if key == current_key:
		current_count += count
	else:
		if current_count > highest_count:
			highest_count = current_count
			highest_count_key = current_key

		current_key = key
		current_count = count

print("%s\t%d" % (highest_count_key, highest_count))