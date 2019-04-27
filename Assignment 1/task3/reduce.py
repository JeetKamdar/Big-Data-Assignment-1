#!/usr/bin/env python

import sys

current_licence_type = None
total_due = 0
licence_type = None
count = 0.0

for line in sys.stdin:
	line = line.strip()
	licence_type, due = line.split("\t")
	try:
		due = float(due)
	except ValueError:
		continue

	if licence_type == current_licence_type:
		total_due += due
		count += 1.0
	else:
		if current_licence_type:
			print("%s\t%.2f, %.2f" % (current_licence_type, total_due, total_due/count))
		current_licence_type = licence_type
		total_due = due
		count = 1.0

if current_licence_type == licence_type:
	print("%s\t%.2f, %.2f" % (current_licence_type,total_due, total_due/count))