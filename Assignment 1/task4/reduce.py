#!/usr/bin/env python

import sys
import string

ny_count = 0
other_count = 0

for line in sys.stdin:
	line = line.strip()
	key,count = line.split("\t")

	try:
		count = int(count)
	except ValueError:
		continue

	if "NY" in key.upper():
		ny_count += count
	else:
		other_count += count



print("NY\t" + str(ny_count))
print("Other\t" + str(other_count))