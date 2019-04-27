#!/usr/bin/env python

import sys
import string
import re

for line in sys.stdin:

	if '"' in line:
		entry = re.split(''',(?=(?:[^'"]|'[^']*'|"[^"]*")*$)''', line)
	else:
		entry = line.split(",")

	licence_type = entry[2]
	amount_due = entry[-6]

	print("%s\t%s" % (licence_type, amount_due))
