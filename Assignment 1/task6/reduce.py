#!/usr/bin/env python

import sys
import string
from collections import OrderedDict

current_key = None
current_count = 0
highest_keys = OrderedDict()
highest_keys["sample_1"] = 0

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
		if current_count > list(highest_keys.values())[-1]:
			if len(highest_keys) >= 20:
				del highest_keys[list(highest_keys.keys())[-1]]
			highest_keys[current_key] = current_count

		highest_keys = OrderedDict(sorted(highest_keys.items(), reverse = True, key=lambda t: t[1]))
		current_key = key
		current_count = count

for key in highest_keys.keys():
	print("%s\t%d" % (key, highest_keys[key]))