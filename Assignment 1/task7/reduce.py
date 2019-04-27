#!/usr/bin/env python

import sys
import os

NUMBER_OF_WEEK_DAYS = 23.00
NUMBER_OF_WEEKEND_DAYS = 8.00
current_code = None
week_day_count = 0
weekend_count = 0

for line in sys.stdin:
	
	line = line.strip()
	code, issue_date, count = line.split("\t", 2)

	try:
		count = int(count)
		day = int(issue_date[8:10])
	except ValueError:
		continue

	if code == current_code:
		if (day % 7 == 5) or (day % 7 == 6):
			weekend_count += count
		else:
			week_day_count += count
	else :
		if current_code:
			print("%s\t%.2f, %.2f" % (current_code, weekend_count / NUMBER_OF_WEEKEND_DAYS, week_day_count/ NUMBER_OF_WEEK_DAYS))
		
		current_code = code
		
		if (day % 7 == 5) or (day % 7 == 6):
			weekend_count = count
			week_day_count = 0
		else:
			week_day_count = count
			weekend_count = 0

if current_code == code:
	print("%s\t%.2f, %.2f" % (current_code, weekend_count / NUMBER_OF_WEEKEND_DAYS, week_day_count/ NUMBER_OF_WEEK_DAYS))