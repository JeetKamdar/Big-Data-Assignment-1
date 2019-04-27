#!/usr/bin/env python

import sys
import string

parking_violation_value = None
current_key = None

for line in sys.stdin:
	line = line.strip()
	key, value = line.split('\t',1)

	if key == current_key:
		parking_violation_value = None
		current_key = None
	else:
		if parking_violation_value:
			if parking_violation_value[-1] == 'P':
				print ("%s\t%s" % (current_key, parking_violation_value[:-3]))
		parking_violation_value = value
		current_key = key
