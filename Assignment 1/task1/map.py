#!/usr/bin/env python

import sys
import os
import string
import re

for line in sys.stdin:
	
	line = line.strip()
	
	if '"' in line:
		entry = re.split(''',(?=(?:[^'"]|'[^']*'|"[^"]*")*$)''', line)
	else:
		entry = line.split(",")

	if  "parking" in os.getenv("mapreduce_map_input_file"):
		summons_number = entry[0].strip()
		issue_date = entry[1].strip()
		violation_code = entry[2].strip()
		plate_id= entry[-8].strip().replace('"','')
		violation_precinct = entry[-16].strip()

		print ("%s\t%s, %s, %s, %s, P" %  (summons_number, plate_id, violation_precinct, violation_code, issue_date))
	
	elif "open" in os.getenv("mapreduce_map_input_file"):
		print ("%s\tO" % entry[0])
	