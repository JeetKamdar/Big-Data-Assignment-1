#!/usr/bin/env python

import sys
import string

for line in sys.stdin:
	
	line.strip()
	entry = line.split(",")

	issue_date, violation_code = entry[1:3]
	
	if issue_date[5:7] == "03":
		print ("%s\t%s\t1" % (violation_code.strip(),issue_date.strip()))